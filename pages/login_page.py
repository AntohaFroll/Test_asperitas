import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = "https://asperitas.vercel.app/login"

    LOCATOR_LOG_IN_BUTTON = '//a[@href="/login"]'
    LOCATOR_USER_NAME_FIELD = '//input[@type="text"]'
    LOCATOR_PASSWORD_FIELD = '//input[@type="password"]'
    LOCATOR_LOG_IN_FORM_BUTTON = '//button[@type="submit"]'
    LOCATOR_REQUIRED_MESSAGE = '//span[text()="required"]'

    def log_in_valid(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOG_IN_BUTTON).click()
        self.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("AntohaFroll")
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("qwerty123456")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        create_post_button = self.driver.find_elements(By.XPATH, '//a[contains(@class, "jEpBlT")]')
        assert len(create_post_button) == 1, "Authorization failed!"

        time.sleep(5)

    def log_in_invalid(self):
        self.driver.implicitly_wait(5)
        button_log_in = self.driver.find_element(By.XPATH, '//a[@href="/login"]')
        button_log_in.click()
        button_log_in_form = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_log_in_form.click()
        assert len(self.driver.find_elements(By.XPATH, '//span[text()="required"]')) == 2,\
            "Authorization failed!"

        time.sleep(5)
