import pytest
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAuthorization:

    def test_user_log_in(self, driver):

        button_log_in = driver.find_element(By.XPATH, '//a[@href="/login"]')
        button_log_in.click()
        input_username = driver.find_element(By.XPATH, '(//input[@type="text"])[1]')
        input_username.send_keys("AntohaFroll")
        input_password = driver.find_element(By.XPATH, '//input[@type="password"]')
        input_password.send_keys("qwerty123456")
        button_log_in_form = driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_log_in_form.click()

    # def test_valid_credentials(self, driver):
    #     pass
    #     # button_log_in = driver.find_element(By.XPATH, '//a[@href="/login"]')
    #     # button_log_in.click()
    #     # input_username = driver.find_element(By.XPATH, '//input[@type="text"]')
    #     # input_username.send_keys("AntohaFroll")
    #     # input_password = driver.find_element(By.XPATH, '//input[@type="password"]')
    #     # input_password.send_keys("qwerty123456")
    #     # button_log_in_form = driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     # button_log_in_form.click()
    #     # user_log_in = WebDriverWait(driver, 10).until(
    #     #          EC.presence_of_element_located((By.CLASS_NAME, 'Text__HeaderUsernameText-sc-2d19d0-0.btUmNk')))
    #
    # def test_invalid_credentials(self, driver):
    #     pass
