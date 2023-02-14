from .base_page import BasePage
from .locators import SignupPageLocators
from .locators import BasePageLocators

class SignupPage(BasePage):
    INVALID_USERNAME = "$"
    SHORT_PASSWORD = "q"
    INVALID_PASSWORD = "qwerty123456"

    def signup_valid(self, generate_username, generate_password):
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert self.wait_element_present(*BasePageLocators.CREATE_POST_LINK), \
            "Registration failed (valid values)!"

    def signup_invalid(self, generate_username, generate_password):
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert len(self.driver.find_elements(*SignupPageLocators.REQUIRED_MESSAGE)) == 2, \
            "Signup failed (no values)!"

        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(self.INVALID_USERNAME)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert len(self.driver.find_elements(*SignupPageLocators.CONTAINS_INVALID_CHARACTERS_MESSAGE)) == 1, \
            "Signup failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert len(self.driver.find_elements(*SignupPageLocators.REQUIRED_MESSAGE)) == 1, \
            "Signup failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(self.SHORT_PASSWORD)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert len(self.driver.find_elements(*SignupPageLocators.MUST_BE_MORE_THAN_8_CHARACTERS_MESSAGE)) == 1, \
            "Signup failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert len(self.driver.find_elements(*SignupPageLocators.PASSWORD_MUST_MATCH_MESSAGE)) == 1, \
            "Signup failed (password not match)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(generate_username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(self.INVALID_PASSWORD)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        assert len(self.driver.find_elements(*SignupPageLocators.PASSWORD_MUST_MATCH_MESSAGE)) == 1, \
            "Signup failed (password not match)!"
