from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    INVALID_USERNAME = "$"
    SHORT_PASSWORD = "q"
    INVALID_PASSWORD = "qwerty123456"
    # LOCATOR_HEADER_USERNAME = f'//span[text()="{user.username}"]'

    def login_valid(self, user):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert self.wait_element_present(*BasePageLocators.CREATE_POST_LINK), \
            "Registration failed (valid values)!"

    def login_invalid(self, user):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert len(self.driver.find_elements(*LoginPageLocators.REQUIRED_MESSAGE)) == 2, \
            "Login failed (no values)!"

        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(self.INVALID_USERNAME)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert len(self.driver.find_elements(*LoginPageLocators.CONTAINS_INVALID_CHARACTERS_MESSAGE)) == 1, \
            "Login failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert len(self.driver.find_elements(*LoginPageLocators.REQUIRED_MESSAGE)) == 1, \
            "Login failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.SHORT_PASSWORD)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert len(self.driver.find_elements(*LoginPageLocators.MUST_BE_MORE_THAN_8_CHARACTERS_MESSAGE)) == 1, \
            "Login failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.INVALID_PASSWORD)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        header_username = self.driver.find_elements(By.XPATH, f'//span[text()="{user.username}"]')
        assert len(header_username) == 0, "Login failed (invalid password)!"
