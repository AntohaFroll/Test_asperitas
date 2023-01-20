import pytest
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://asperitas.vercel.app/"


class TestRegistration:

    def test_valid_credentials(self, driver):
        driver.get(url)
        button_sign_up = driver.find_element(By.XPATH, '//a[@href="/signup"]')
        button_sign_up.click()
        input_username = driver.find_element(By.XPATH, '//input[@name="username"]')
        username = uuid.uuid4().__str__().split("-")[-1]
        input_username.send_keys(username)
        input_password = driver.find_element(By.XPATH, '//input[@name="password"]')
        password = uuid.uuid4().__str__().split("-")[-1]
        input_password.send_keys(password)
        input_password2 = driver.find_element(By.XPATH, '//input[@name="password2"]')
        input_password2.send_keys(password)
        button_sign_up_form = driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_sign_up_form.click()
        # WebDriverWait(browser, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '//span[text()=username]')), message = "Registration failed")
        user_log_in = driver.find_elements(By.XPATH, '//a[@href="/login"]')
        assert len(user_log_in) == 0, "Registration failed"

    def test_invalid_credentials(self, driver):
        driver.get(url)
        button_sign_up = driver.find_element(By.XPATH, '//a[@href="/signup"]')
        button_sign_up.click()
        input_username = driver.find_element(By.XPATH, '//input[@name="username"]')
        input_username.send_keys("Antoha$Froll")
        button_sign_up_form = driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_sign_up_form.click()
        invalid_characters_hint = driver.find_elements(By.XPATH, '//span[text()="contains invalid characters"]')
        assert len(invalid_characters_hint) == 1
