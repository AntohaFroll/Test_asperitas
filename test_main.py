import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_open_site(driver):
    base_page = BasePage(driver)

    base_page.open()

    base_page.should_page_open()


def test_signup_valid(driver):
    base_page = BasePage(driver)
    signup_page = SignupPage(driver)

    base_page.open()

    signup_page.signup_valid()


def test_signup_invalid(driver):
    base_page = BasePage(driver)
    signup_page = SignupPage(driver)

    base_page.open()

    signup_page.signup_invalid()


@pytest.mark.only
def test_login_valid(driver):
    base_page = BasePage(driver)
    login_page = LoginPage(driver)

    base_page.open()

    login_page.login_valid()


def test_login_invalid(driver):
    base_page = BasePage(driver)
    login_page = LoginPage(driver)

    base_page.open()

    login_page.login_invalid()
