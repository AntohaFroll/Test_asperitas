import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.post_page import PostPage


def test_open_site(driver):
    base_page = BasePage(driver)
    base_page.open()
    base_page.should_be_open_page()


class TestsSignup:
    def test_signup_valid(self, driver):
        base_page = BasePage(driver)
        signup_page = SignupPage(driver)
        base_page.open()
        signup_page.signup_valid()

    def test_signup_invalid(self, driver):
        base_page = BasePage(driver)
        signup_page = SignupPage(driver)
        base_page.open()
        signup_page.signup_invalid()


class TestsLogin:
    def test_login_valid(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        base_page.open()
        login_page.login_valid(new_user)

    def test_login_invalid(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        base_page.open()
        login_page.login_invalid(new_user)


class TestsPost:
    def test_create_text_post(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        login_page.login_valid(new_user)
        post_page.create_text_post()

    def test_delete_post(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        login_page.login_valid(new_user)
        post_page.create_text_post()
        post_page.delete_post()


class TestsComment:
    def test_create_comment(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        login_page.login_valid(new_user)
        post_page.create_comment()

    @pytest.mark.only
    def test_delete_comment(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        login_page.login_valid(new_user)
        post_page.create_comment()
        post_page.delete_comment()
