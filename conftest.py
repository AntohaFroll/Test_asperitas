import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    print("\nstart browser for test")
    driver = webdriver.Chrome()

    yield driver

    print("\nquit browser")
    driver.quit()
