import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.post_page import PostPage


@pytest.mark.smoke
def test_open_site(driver):
    base_page = BasePage(driver)
    base_page.open()
    base_page.should_be_open_page()


@pytest.mark.signup
class TestsSignup:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.go_to_signup_page()

    def test_signup_valid(self, driver, generate_unique_string, generate_password):
        signup_page = SignupPage(driver)
        signup_page.entry_valid_date(generate_unique_string, generate_password)
        signup_page.should_be_authorized_user()

    def test_empty_fields(self, driver):
        signup_page = SignupPage(driver)
        signup_page.empty_fields()
        signup_page.should_be_massage_required()

    def test_invalid_username_and_empty_password_field(self, driver):
        signup_page = SignupPage(driver)
        signup_page.entry_invalid_username_and_empty_password_field()
        signup_page.should_be_message_contains_invalid_characters()

    def test_valid_username_and_empty_password_field(self, driver, generate_unique_string):
        signup_page = SignupPage(driver)
        signup_page.entry_valid_username_and_empty_password_field(generate_unique_string)
        signup_page.should_be_massage_required()

    def test_valid_username_and_short_password(self, driver, generate_unique_string, generate_password):
        signup_page = SignupPage(driver)
        signup_page.entry_valid_username_and_short_password(generate_unique_string, generate_password)
        signup_page.should_be_message_most_be_more_than_8_characters()

    def test_entry_valid_username_password_and_7_signs_password(self, driver, generate_unique_string,
                                                                generate_password):
        signup_page = SignupPage(driver)
        signup_page.entry_valid_username_password_and_7_signs_confirm_password(generate_unique_string,
                                                                               generate_password)
        signup_page.should_be_message_most_be_more_than_8_characters()

    def test_entry_valid_username_password_and_empty_confirm_password_field(self, driver, generate_unique_string,
                                                                            generate_password):
        signup_page = SignupPage(driver)
        signup_page.entry_valid_username_password_and_empty_confirm_password_field(generate_unique_string,
                                                                                   generate_password)
        signup_page.should_be_message_password_must_match()

    def test_entry_valid_username_password_and_invalid_confirm_password_field(self, driver, generate_unique_string,
                                                                              generate_password):
        signup_page = SignupPage(driver)
        signup_page.entry_valid_username_password_and_invalid_confirm_password_field(generate_unique_string,
                                                                                     generate_password)
        signup_page.should_be_message_password_must_match()


class TestsLogin:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.go_to_login_page()

    def test_login_valid(self, driver, new_user):
        login_page = LoginPage(driver)
        login_page.entry_valid_data(new_user)
        login_page.should_be_authorized_user()

    def test_login_invalid(self, driver, new_user, generate_password):
        login_page = LoginPage(driver)
        login_page.empty_fields()
        login_page.should_be_required_massage()
        login_page.entry_invalid_data(new_user, generate_password)


class TestsPostAndComment:
    @pytest.mark.post
    class TestsPost:
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, driver, new_user):
            base_page = BasePage(driver)
            login_page = LoginPage(driver)
            base_page.open()
            base_page.go_to_login_page()
            login_page.entry_valid_data(new_user)
            login_page.should_be_authorized_user()
            base_page.go_to_create_post_page()

        def test_create_text_post(self, driver, generate_unique_string):
            post_page = PostPage(driver)
            post_page.create_text_post(generate_unique_string)
            post_page.should_be_post_created()

        def test_create_url_post(self, driver, generate_unique_string, generate_url):
            post_page = PostPage(driver)
            post_page.create_url_post(generate_unique_string, generate_url)
            post_page.should_be_post_created()

        def test_delete_post(self, driver, generate_unique_string):
            post_page = PostPage(driver)
            post_page.create_text_post(generate_unique_string)
            post_page.should_be_post_created()
            post_page.delete_post()
            post_page.should_be_post_deleted()

    @pytest.mark.comment
    class TestsComment:
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, driver, new_user):
            base_page = BasePage(driver)
            login_page = LoginPage(driver)
            base_page.open()
            base_page.go_to_login_page()
            login_page.entry_valid_data(new_user)
            login_page.should_be_authorized_user()

        def test_create_comment(self, driver, generate_unique_string):
            post_page = PostPage(driver)
            post_page.create_comment(generate_unique_string)
            post_page.should_be_comment_created()

        def test_delete_comment(self, driver, generate_unique_string):
            post_page = PostPage(driver)
            post_page.create_comment(generate_unique_string)
            post_page.delete_comment()
            post_page.should_be_comment_deleted()
