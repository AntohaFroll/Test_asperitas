from .base_page import BasePage
from .locators import SignupPageLocators
from .locators import BasePageLocators


class SignupPage(BasePage):
    def entry_valid_date(self, generate_username, generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_of_element_present(*BasePageLocators.CREATE_POST_LINK), \
            "Registration failed (valid values)!"

    def should_be_authorized_user(self):
        assert self.wait_of_element_present(*BasePageLocators.CREATE_POST_LINK), \
            "Login failed (valid values)!"

    def empty_fields(self):
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    def should_be_required_massage(self):
        assert self.wait_of_element_present(*SignupPageLocators.REQUIRED_MESSAGE), \
            "Login failed (no value/values)!"

    def entry_invalid_username_and_empty_password_field(self):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys("$#%")
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    def entry_valid_username_and_empty_password_field(self, generate_username):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    # TODO если у тебя в названии метода 2 глагола (be и contains),
    # TODO то метод должен называться should_contain
    def should_be_contains_invalid_characters_message(self):
        assert self.wait_of_element_present(*SignupPageLocators.CONTAINS_INVALID_CHARACTERS_MESSAGE), \
            "Signup failed (invalid user name)!"

    def entry_valid_username_and_short_password(self, generate_username, generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password[0])
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    def entry_valid_username_password_and_7_signs_confirm_password(self, generate_username,
                                                                   generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password[0:7])
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    # TODO тут should_be_longer_than_8_characters
    def should_be_most_be_more_than_8_characters_message(self):
        assert self.wait_of_element_present(*SignupPageLocators.MUST_BE_MORE_THAN_8_CHARACTERS_MESSAGE), \
            "Signup failed (short password)!"

    def entry_valid_username_password_and_empty_confirm_password_field(self, generate_username,
                                                                       generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    def entry_valid_username_password_and_invalid_confirm_password_field(self, generate_username,
                                                                         generate_password, generate_text):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(generate_text)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    def should_be_password_must_match_message(self):
        assert self.wait_of_element_present(*SignupPageLocators.PASSWORD_MUST_MATCH_MESSAGE), \
            "Signup failed (password not match)!"
