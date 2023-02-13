from .base_page import BasePage
from .locators import SignupPageLocators
import uuid


class SignupPage(BasePage):
    INVALID_USERNAME = "$"
    SHORT_PASSWORD = "q"
    INVALID_PASSWORD = "qwerty123456"
    username = uuid.uuid4().__str__().split("-")[-1]
    password = uuid.uuid4().__str__().split("-")[-1]

    def signup_valid(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(self.username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(self.password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(self.password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON_IN_FORM).click()
        create_post_button = self.driver.find_elements(*SignupPageLocators.CREATE_POST_BUTTON)
        assert len(create_post_button) == 1, "Registration failed (valid values)!"

    def signup_invalid(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON_IN_FORM).click()
        assert len(self.driver.find_elements(*SignupPageLocators.REQUIRED_MESSAGE)) == 2, \
            "Signup failed (no values)!"

        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(self.INVALID_USERNAME)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON_IN_FORM).click()
        assert len(self.driver.find_elements(*SignupPageLocators.CONTAINS_INVALID_CHARACTERS_MESSAGE)) == 1, \
            "Signup failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(self.username)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON_IN_FORM).click()
        assert len(self.driver.find_elements(*SignupPageLocators.REQUIRED_MESSAGE)) == 1, \
            "Signup failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(self.username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(self.SHORT_PASSWORD)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON_IN_FORM).click()
        assert len(self.driver.find_elements(*SignupPageLocators.MUST_BE_MORE_THAN_8_CHARACTERS_MESSAGE)) == 1, \
            "Signup failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(self.username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(self.password)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON_IN_FORM).click()
        assert len(self.driver.find_elements(*SignupPageLocators.PASSWORD_MUST_MATCH_MESSAGE)) == 1, \
            "Signup failed (password not match)!"

        self.driver.refresh()
        self.driver.find_element(*SignupPageLocators.USERNAME_FIELD).send_keys(self.username)
        self.driver.find_element(*SignupPageLocators.PASSWORD_FIELD).send_keys(self.password)
        self.driver.find_element(*SignupPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(self.INVALID_PASSWORD)
        self.driver.find_element(*SignupPageLocators.SIGNUP_BUTTON_IN_FORM).click()
        assert len(self.driver.find_elements(*SignupPageLocators.PASSWORD_MUST_MATCH_MESSAGE)) == 1, \
            "Signup failed (password not match)!"
