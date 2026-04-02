import pytest
from pages.cookie_page.ing_cookie_page import IngCookiePage


@pytest.fixture()
def cookie_page(page):
    return IngCookiePage(page)
