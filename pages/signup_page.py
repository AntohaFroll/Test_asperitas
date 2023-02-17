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

    def should_be_required_massage(self):
        assert self.wait_of_element_present(*SignupPageLocators.REQUIRED_MESSAGE), \
            "Login failed (no values)!"

    def empty_fields(self):
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    def entry_invalid_date(self, generate_username, generate_password, generate_text):
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_of_element_present(*SignupPageLocators.REQUIRED_MESSAGE), \
            "Signup failed (no values)!"

        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys("$#%")
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_of_element_present(*SignupPageLocators.CONTAINS_INVALID_CHARACTERS_MESSAGE), \
            "Signup failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_of_element_present(*SignupPageLocators.REQUIRED_MESSAGE), \
            "Signup failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password[0])
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_of_element_present(*SignupPageLocators.MUST_BE_MORE_THAN_8_CHARACTERS_MESSAGE), \
            "Signup failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_of_element_present(*SignupPageLocators.PASSWORD_MUST_MATCH_MESSAGE), \
            "Signup failed (password not match)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(generate_text)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_of_element_present(*SignupPageLocators.PASSWORD_MUST_MATCH_MESSAGE), \
            "Signup failed (password not match)!"
