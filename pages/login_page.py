from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    LOCATOR_LOG_IN_BUTTON = '//a[@href="/login"]'
    LOCATOR_USER_NAME_FIELD = '//input[@name="username"]'
    LOCATOR_PASSWORD_FIELD = '//input[@name="password"]'
    LOCATOR_CONFIRM_PASSWORD_FIELD = '//input[@name="password2"]'
    LOCATOR_LOG_IN_FORM_BUTTON = '//button[@type="submit"]'
    LOCATOR_REQUIRED_MESSAGE = '//span[text()="required"]'
    LOCATOR_CONTAINS_INVALID_CHARACTERS = '//span[text()="contains invalid characters"]'
    LOCATOR_MUST_BE_MORE_THAN_8_CHARACTERS = '//span[text()="must be more than 8 characters"]'
    USER_NAME = "AntohaFroll"
    USER_PASSWORD = "qwerty123456"

    def log_in_valid(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_BUTTON).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys(self.USER_PASSWORD)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_FORM_BUTTON).click()
        create_post_button = self.driver.find_elements(By.XPATH, '//a[contains(@class, "jEpBlT")]')
        assert len(create_post_button) == 1, "Authorization failed (valid values)!"

    def log_in_invalid(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_BUTTON).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_REQUIRED_MESSAGE)) == 2, \
            "Authorization failed (no values)!"
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys("Antoha$roll")
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_CONTAINS_INVALID_CHARACTERS)) == 1, \
            "Authorization failed (invalid user name)!"
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_REQUIRED_MESSAGE)) == 1, \
            "Authorization failed (no password)!"
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys("q")
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_MUST_BE_MORE_THAN_8_CHARACTERS)) == 1, \
            "Authorization failed (short password)!"
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys("qwerty123457")
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_FORM_BUTTON).click()
        create_post_button = self.driver.find_elements(By.XPATH, '//a[contains(@class, "jEpBlT")]')
        assert len(create_post_button) == 0, "Authorization failed (invalid password)!"
        time.sleep(3)
