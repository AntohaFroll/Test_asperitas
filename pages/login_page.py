import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_LOG_IN_BUTTON = (By.XPATH, '//a[@href="/login"]')
    LOCATOR_USER_NAME_FIELD = (By.XPATH, '//input[@type="text"]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    LOCATOR_LOG_IN_FORM_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOCATOR_REQUIRED_MESSAGE = (By.XPATH, '//span[text()="required"]')


class LoginPage(BasePage):

    def log_in_valid(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        self.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("AntohaFroll")
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("qwerty123456")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        create_post_button = self.driver.find_elements(By.XPATH, '//a[@href="/createpost"]')
        assert len(create_post_button) != 0, "Authorization failed!"

        time.sleep(5)

    def log_in_invalid(self):
        self.driver.implicitly_wait(5)
        button_log_in = self.driver.find_element(By.XPATH, '//a[@href="/login"]')
        button_log_in.click()
        button_log_in_form = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_log_in_form.click()
        assert len(self.driver.find_elements(By.XPATH, '//span[text()="required"]')) == 1,\
            "Authorization failed!"

        time.sleep(5)
