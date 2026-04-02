import pytest
from playwright.sync_api import sync_playwright
from tests.conftest import IngCookiePage


def test_ing_analytics_cookie_is_saved(cookie_page, context, browser_name):
    cookie_page.open_url()
    cookie_page.customize_cookies_button()
    cookie_page.switch_toggle_analytics_cookies()

    assert cookie_page.is_analytics_toggle_checked(), (
        f"[{browser_name}] Toggle analityczny nie jest zaznaczony po kliknięciu"
    )

    cookie_page.accept_selected()

    cookies = cookie_page.get_all_cookies(context)

    session_cookie_policy_gdpr_details = cookie_page.get_cookie_by_name(
        cookies, "cookiePolicyGDPR__details"
    )
    session_cookie_policy_gdpr = cookie_page.get_cookie_by_name(
        cookies, "cookiePolicyGDPR"
    )

    assert session_cookie_policy_gdpr_details is not None, (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR__details' nie zostało zapisane"
    )
    assert session_cookie_policy_gdpr is not None, (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR' nie zostało zapisane"
    )
    assert session_cookie_policy_gdpr_details["name"] == "cookiePolicyGDPR__details", (
        f"[{browser_name}] Cookie name: 'cookiePolicyGDPR__details' ma niepoprawną wartość!"
    )
    assert session_cookie_policy_gdpr["name"] == "cookiePolicyGDPR", (
        f"[{browser_name}] Cookie name: 'cookiePolicyGDPR' ma niepoprawną wartość!"
    )
    assert session_cookie_policy_gdpr["value"] == "3", (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR' powinno mieć wartość '3', "
        f"a ma '{session_cookie_policy_gdpr['value']}'"
    )
    assert "cookieCreateTimestamp" in session_cookie_policy_gdpr_details["value"], (
        f"[{browser_name}] Cookie 'cookiePolicyGDPR__details' nie zawiera 'cookieCreateTimestamp'"
    )

