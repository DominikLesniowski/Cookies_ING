from playwright.sync_api import sync_playwright

def test_ing_cookie_consent():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:  
            browser = browser_type.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.ing.pl")

            page.get_by_role("button", name="Dostosuj").click()
            page.get_by_role("switch", name="Cookies analityczne").locator("span").nth(1).click()
            page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
            cookies = context.cookies()

            def get_cookie_by_name(cookies, name):
                return next((cookie for cookie in cookies if cookie["name"] == name), None)

            session_cookie = get_cookie_by_name(cookies, "cookiePolicyGDPR__details")
            session_cookie2 = get_cookie_by_name(cookies, "cookiePolicyGDPR")
            
            assert session_cookie["name"] == "cookiePolicyGDPR__details", "Cookie name: 'cookiePolicyGDPR__details' ma niepoprawną wartość!"
            assert session_cookie2["name"] == "cookiePolicyGDPR", "Cookie name: 'cookiePolicyGDPR' ma niepoprawną wartość!"
            assert session_cookie2["value"] == "3", "Cookie 'cookiePolicyGDPR' ma niepoprawną wartość!"
            assert "cookieCreateTimestamp" in session_cookie["value"], "Cookie 'cookiePolicyGDPR__details' ma niepoprawną wartość!"
            page.wait_for_timeout(500)
            print('Pozytywnie zweryfikowane cookies')
            browser.close()