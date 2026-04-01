from playwright.sync_api import Page


def button_customize(page: Page):
    return page.get_by_role("button", name="Dostosuj")


def switch_analytics_cookies(page: Page):
    return page.get_by_role("switch", name="Cookies analityczne")


def button_accept_selected(page: Page):
    return page.get_by_role("button", name="Zaakceptuj zaznaczone")


def _toggle_analytics_locator(page: Page):
    return page.locator('div[name="CpmAnalyticalOption"]')


def is_toggle_analytics_checked(page: Page) -> bool:
    toggle = _toggle_analytics_locator(page)
    aria_checked = toggle.get_attribute("aria-checked")
    return aria_checked == "true"
