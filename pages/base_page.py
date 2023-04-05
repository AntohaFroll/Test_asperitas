from .locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    url = "https://asperitas.vercel.app/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def go_to(self, url):
        self.driver.get(url)

    def should_be_open_page(self):
        assert self.is_element_present(*BasePageLocators.LOGO), \
            "Page don't open!"

    def is_element_disappeared(self, how, what, timeout=3):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.driver, 3). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_to_be_clickable(self, how, what):
        try:
            WebDriverWait(self.driver, 3). \
                until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True
