import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    print("\nstart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser")
    driver.quit()
