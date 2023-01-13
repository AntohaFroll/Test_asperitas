import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
link = "https://asperitas.vercel.app/"

class TestRegistration():


    def test_registration_correct(self, browser):
        browser.get(link)
        button_sign_up = browser.find_element(By.CSS_SELECTOR, "#root > header > a:nth-child(4)")
        button_sign_up.click()
        input_username = browser.find_element(By.NAME, "username")
        input_username.send_keys("AntohaFroll")
        input_password = browser.find_element(By.NAME, "password")
        input_password.send_keys("qwerty123456")
        input_password2 = browser.find_element(By.NAME, "password2")
        input_password2.send_keys("qwerty123456")
        button_sign_up_form = browser.find_element(By.CLASS_NAME, "Button-sc-1mhyaz8-0")
        button_sign_up_form.click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Text__HeaderUsernameText-sc-2d19d0-0.btUmNk")))

    @pytest.mark.only
    def test_registration_incorrect(self, browser):
        browser.get(link)
        button_sign_up = browser.find_element(By.CSS_SELECTOR, "#root > header > a:nth-child(4)")
        button_sign_up.click()
        input_username = browser.find_element(By.NAME, "username")
        input_username.send_keys("АнтохаФролл")
        input_password = browser.find_element(By.NAME, "password")
        input_password.send_keys("qwerty123456")
        input_password2 = browser.find_element(By.NAME, "password2")
        input_password2.send_keys("qwerty123456")
        button_sign_up_form = browser.find_element(By.CLASS_NAME, "Button-sc-1mhyaz8-0")
        button_sign_up_form.click()
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Text__HeaderUsernameText-sc-2d19d0-0.btUmNk")))