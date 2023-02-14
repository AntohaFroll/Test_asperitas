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
    def test_signup_valid(self, driver, generate_username, generate_password):
        base_page = BasePage(driver)
        signup_page = SignupPage(driver)
        base_page.open()
        base_page.go_to_signup_page()
        signup_page.signup_valid(generate_username, generate_password)

    def test_signup_invalid(self, driver, generate_username, generate_password):
        base_page = BasePage(driver)
        signup_page = SignupPage(driver)
        base_page.open()
        base_page.go_to_signup_page()
        signup_page.signup_invalid(generate_username, generate_password)


class TestsLogin:
    def test_login_valid(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        base_page.open()
        base_page.go_to_login_page()
        login_page.login_valid(new_user)

    def test_login_invalid(self, driver, new_user):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        base_page.open()
        base_page.go_to_login_page()
        login_page.login_invalid(new_user)

@pytest.mark.only
class TestsPost:
    def test_create_text_post(self, driver, new_user, generate_text):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        base_page.go_to_login_page()
        login_page.login_valid(new_user)
        base_page.go_to_create_post_page()
        post_page.create_text_post(generate_text)

    def test_delete_post(self, driver, new_user, generate_text):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        base_page.go_to_login_page()
        login_page.login_valid(new_user)
        base_page.go_to_create_post_page()
        post_page.create_text_post(generate_text)
        post_page.delete_post()


class TestsComment:
    def test_create_comment(self, driver, new_user, generate_text):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        base_page.go_to_login_page()
        login_page.login_valid(new_user)
        post_page.create_comment(generate_text)

    def test_delete_comment(self, driver, new_user, generate_text):
        base_page = BasePage(driver)
        login_page = LoginPage(driver)
        post_page = PostPage(driver)
        base_page.open()
        base_page.go_to_login_page()
        login_page.login_valid(new_user)
        post_page.create_comment(generate_text)
        post_page.delete_comment()
