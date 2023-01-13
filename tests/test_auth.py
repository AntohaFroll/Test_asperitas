import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://asperitas.vercel.app/"

class TestAuthorization():


    def test_authorization_correct(self, browser):
        browser.get(link)
        button_log_in = browser.find_element(By.CSS_SELECTOR, "#root > header > a:nth-child(3)")
        button_log_in.click()
        input_username = browser.find_element(By.NAME, "username")
        input_username.send_keys("AntohaFroll")
        input_password = browser.find_element(By.NAME, "password")
        input_password.send_keys("qwerty123456")
        button_log_in_form = browser.find_element(By.CLASS_NAME, "Button-sc-1mhyaz8-0")
        button_log_in_form.click()
        WebDriverWait(browser, 10).until(
                 EC.presence_of_element_located((By.CLASS_NAME, "Text__HeaderUsernameText-sc-2d19d0-0.btUmNk")))

    def test_authorization_incorrect(self, browser):
        pass
