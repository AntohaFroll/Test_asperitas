from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    LOCATOR_LOGIN_BUTTON = '//a[@href="/login"]'
    LOCATOR_USER_NAME_FIELD = '//input[@name="username"]'
    LOCATOR_PASSWORD_FIELD = '//input[@name="password"]'
    LOCATOR_LOGIN_FORM_BUTTON = '//button[@type="submit"]'
    LOCATOR_REQUIRED_MESSAGE = '//span[text()="required"]'
    LOCATOR_CONTAINS_INVALID_CHARACTERS = '//span[text()="contains invalid characters"]'
    LOCATOR_MUST_BE_MORE_THAN_8_CHARACTERS = '//span[text()="must be more than 8 characters"]'
    LOCATOR_CREATE_POST_BUTTON = '//a[contains(@class, "jEpBlT")]'
    INVALID_USERNAME = "$"
    SHORT_PASSWORD = "q"
    INVALID_PASSWORD = "qwerty123456"

    def login_valid(self, user):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_BUTTON).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(user.username)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_FORM_BUTTON).click()
        create_post_button = self.driver.find_elements(By.XPATH, self.LOCATOR_CREATE_POST_BUTTON)
        assert len(create_post_button) == 1, "Login failed (valid values)!"

    def login_invalid(self, user):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_BUTTON).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_REQUIRED_MESSAGE)) == 2, \
            "Login failed (no values)!"

        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.INVALID_USERNAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_CONTAINS_INVALID_CHARACTERS)) == 1, \
            "Login failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(user.username)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_REQUIRED_MESSAGE)) == 1, \
            "Login failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(user.username)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys(self.SHORT_PASSWORD)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_MUST_BE_MORE_THAN_8_CHARACTERS)) == 1, \
            "Login failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(user.username)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys(self.INVALID_PASSWORD)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_FORM_BUTTON).click()
        create_post_button = self.driver.find_elements(By.XPATH, self.LOCATOR_CREATE_POST_BUTTON)
        assert len(create_post_button) == 0, "Login failed (invalid password)!"
