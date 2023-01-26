from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import uuid


class SignupPage(BasePage):

    LOCATOR_SIGNUP_BUTTON = '//a[@href="/signup"]'
    LOCATOR_USER_NAME_FIELD = '//input[@name="username"]'
    LOCATOR_PASSWORD_FIELD = '//input[@name="password"]'
    LOCATOR_CONFIRM_PASSWORD_FIELD = '//input[@name="password2"]'
    LOCATOR_SIGNUP_FORM_BUTTON = '//button[@type="submit"]'
    LOCATOR_REQUIRED_MESSAGE = '//span[text()="required"]'
    LOCATOR_CONTAINS_INVALID_CHARACTERS = '//span[text()="contains invalid characters"]'
    LOCATOR_MUST_BE_MORE_THAN_8_CHARACTERS = '//span[text()="must be more than 8 characters"]'
    LOCATOR_PASSWORD_MUST_MATCH = '//span[text()="passwords must match"]'
    USER_NAME = "AntohaFroll"
    USER_PASSWORD = "qwerty123456"

    def signup_valid(self, username, password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_BUTTON).click()
        username = uuid.uuid4().__str__().split("-")[-1]
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(username)
        password = uuid.uuid4().__str__().split("-")[-1]
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(By.XPATH, self.LOCATOR_CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_FORM_BUTTON).click()
        create_post_button = self.driver.find_elements(By.XPATH, '//a[contains(@class, "jEpBlT")]')
        assert len(create_post_button) == 1, "Registration failed (valid values)!"

    def signup_invalid(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_BUTTON).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_REQUIRED_MESSAGE)) == 2, \
            "Signup failed (no values)!"

        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys("Antoha$roll")
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_CONTAINS_INVALID_CHARACTERS)) == 1, \
            "Signup failed (invalid user name)!"

        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_REQUIRED_MESSAGE)) == 1, \
            "Signup failed (no password)!"

        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys("q")
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_MUST_BE_MORE_THAN_8_CHARACTERS)) == 1, \
            "Signup failed (short password)!"

        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys(self.USER_PASSWORD)
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_PASSWORD_MUST_MATCH)) == 1, \
            "Signup failed (password not match)!"

        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME_FIELD).send_keys(self.USER_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_PASSWORD_FIELD).send_keys(self.USER_PASSWORD)
        self.driver.find_element(By.XPATH, self.LOCATOR_CONFIRM_PASSWORD_FIELD).send_keys("qwerty123457")
        self.driver.find_element(By.XPATH, self.LOCATOR_SIGNUP_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_PASSWORD_MUST_MATCH)) == 1, \
            "Signup failed (password not match)!"
