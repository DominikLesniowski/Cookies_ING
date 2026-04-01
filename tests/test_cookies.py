import pytest
from playwright.sync_api import sync_playwright
from pages.cookie_page.ing_cookie_page import IngCookiePage



@pytest.fixture()
def browser_context(target_browser):

    with sync_playwright() as p:
        browser_type = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit,
        }[target_browser]

        browser = browser_type.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page, context

        context.close()
        browser.close()


@pytest.fixture()
def cookie_page(page):
    return IngCookiePage(page)


def test_ing_analytics_cookie_is_saved(cookie_page, context, browser_name):
    cookie_page.open_url()
    cookie_page.customize_cookies_button()
    cookie_page.switch_toggle_analytics_cookies()

    assert cookie_page.is_analytics_toggle_checked(), (
        f"[{browser_name}] Toggle analityczny nie jest zaznaczony po kliknięciu"
    )

    cookie_page.accept_selected()

    cookies = cookie_page.get_all_cookies(context)

    session_cookie_policyGDPR_details = cookie_page.get_cookie_by_name(
        cookies, "cookiePolicyGDPR__details"
    )
    session_cookie_policyGDPR = cookie_page.get_cookie_by_name(
        cookies, "cookiePolicyGDPR"
    )

    assert session_cookie_policyGDPR_details is not None, (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR__details' nie zostało zapisane"
    )
    assert session_cookie_policyGDPR is not None, (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR' nie zostało zapisane"
    )
    assert session_cookie_policyGDPR_details["name"] == "cookiePolicyGDPR__details", (
        f"[{browser_name}] Cookie name: 'cookiePolicyGDPR__details' ma niepoprawną wartość!"
    )
    assert session_cookie_policyGDPR["name"] == "cookiePolicyGDPR", (
        f"[{browser_name}] Cookie name: 'cookiePolicyGDPR' ma niepoprawną wartość!"
    )
    assert session_cookie_policyGDPR["value"] == "3", (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR' powinno mieć wartość '3', "
        f"a ma '{session_cookie_policyGDPR['value']}'"
    )
    assert "cookieCreateTimestamp" in session_cookie_policyGDPR_details["value"], (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR__details' nie zawiera 'cookieCreateTimestamp'"
    )
