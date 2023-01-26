import pytest
from selenium import webdriver
import requests
import uuid
from entities.user import User


@pytest.fixture
def driver():
    print("\nstart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser")
    driver.quit()


class CreateUser(User):
    
    @pytest.fixture
    def create_user(self, username, password):
        print("\ncreate user")
        self.username = uuid.uuid4().__str__().split("-")[-1]
        self.password = uuid.uuid4().__str__().split("-")[-1]
        url = "https://asperitas.vercel.app/api/register"
        data = {"username": username, "password": password}
        create_user = requests.post(url, json=data)
        return create_user
