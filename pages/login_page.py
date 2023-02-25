from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    url = "https://asperitas.vercel.app/login"

    def go_to_login_page(self):
        self.go_to(self.url)

    def enter_valid_data(self, user):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.CREATE_POST_LINK), \
            "Login failed (valid values)!"

    def should_be_required_massage(self):
        assert self.is_element_present(*LoginPageLocators.MESSAGE_REQUIRED), \
            "Login failed (no values)!"

    def click_to_login_btn(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def enter_invalid_data(self, user, generate_password):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("$#%")
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
        assert self.is_element_present(*LoginPageLocators.MESSAGE_CONTAINS_INVALID_CHARACTERS), \
            "Login failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
        assert self.is_element_present(*LoginPageLocators.MESSAGE_REQUIRED), \
            "Login failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(generate_password[0])
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
        assert self.is_element_present(*LoginPageLocators.MESSAGE_MUST_BE_MORE_THAN_8_CHARACTERS), \
            "Login failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(generate_password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
        assert self.is_element_present(*LoginPageLocators.MESSAGE_INVALID_PASSWORD), \
            "Login failed (invalid password)!"
