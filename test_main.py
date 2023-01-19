from selenium import webdriver
from pages.base_page import BasePage
from pages.login_page import LoginPage

driver = webdriver.Chrome

base_page = BasePage(driver)
log_in_page = LoginPage(driver)


def test_log_in_valid():
    base_page.open()

    base_page.go_to(base_page.login_url)

    log_in_page.log_in_valid()


def test_log_in_invalid():
    base_page.open()

    base_page.go_to(base_page.login_url)

    log_in_page.log_in_invalid()
