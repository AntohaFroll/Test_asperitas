import pytest

from pages.base_page import BasePage
from pages.login_page import LoginPage


def test_log_in_valid(driver):

    base_page = BasePage(driver)
    log_in_page = LoginPage(driver)

    base_page.open()

    base_page.go_to(log_in_page.url)

    log_in_page.log_in_valid()

@pytest.mark.only
def test_log_in_invalid(driver):

    base_page = BasePage(driver)
    log_in_page = LoginPage(driver)

    base_page.open()

    base_page.go_to(log_in_page.url)

    log_in_page.log_in_invalid()
