from playwright.sync_api import Page
from pages.cookie_page.ing_cookie_page_selectors import (
    button_customize,
    switch_analytics_cookies,
    button_accept_selected,
    is_toggle_analytics_checked,
)


class IngCookiePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self):
        self.page.goto("https://www.ing.pl")

    def customize_cookies_button(self):
        button_customize(self.page).click()

    def switch_toggle_analytics_cookies(self):
        switch_analytics_cookies(self.page).click()

    def is_analytics_toggle_checked(self) -> bool:
        return is_toggle_analytics_checked(self.page)

    def accept_selected(self):
        button_accept_selected(self.page).click()

    def get_all_cookies(self, context) -> list:
        return context.cookies()

    def get_cookie_by_name(self, cookies: list, name: str) -> dict | None:
        return next((cookie for cookie in cookies if cookie["name"] == name), None)
