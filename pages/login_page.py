from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):

    def entry_valid_date(self, user):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_authorized_user(self):
        assert self.wait_of_element_present(*BasePageLocators.CREATE_POST_LINK), \
            "Login failed (valid values)!"

    def should_be_required_massage(self):
        assert self.wait_of_element_present(*LoginPageLocators.REQUIRED_MESSAGE), \
            "Login failed (no values)!"

    def empty_fields(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def entry_invalid_date(self, user, generate_username, generate_password):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("$#%")
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert self.wait_of_element_present(*LoginPageLocators.CONTAINS_INVALID_CHARACTERS_MESSAGE), \
            "Login failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert self.wait_of_element_present(*LoginPageLocators.REQUIRED_MESSAGE), \
            "Login failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(generate_password[0])
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert self.wait_of_element_present(*LoginPageLocators.MUST_BE_MORE_THAN_8_CHARACTERS_MESSAGE), \
            "Login failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert self.wait_of_element_present(*LoginPageLocators.INVALID_PASSWORD_MESSAGE), \
            "Login failed (invalid password)!"
