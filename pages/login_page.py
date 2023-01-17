from base_page import BasePage
from selenium.webdriver.common.by import By

class LoginLocators:
    LOCATOR_LOG_IN_BUTTON = (By.XPATH, '//a[@href="/login"]')
    LOCATOR_USER_NAME_FIELD = (By.XPATH, '//input[@type="text"]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    LOCATOR_LOG_IN_FORM_BUTTON = (By.XPATH, '//button[@type="submit"]')

class LoginPage(BasePage):
    def user_log_in(self):
        button_log_in = self.find_element(LoginLocators.LOCATOR_LOG_IN_BUTTON)
        button_log_in.click()
        input_username = self.find_element(LoginLocators.LOCATOR_USER_NAME_FIELD)
        input_username.send_keys("AntohaFroll")
        input_password = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        input_password.send_keys("qwerty123456")
        button_log_in_form = self.find_element(LoginLocators.LOCATOR_LOG_IN_FORM_BUTTON)
        button_log_in_form.click()
