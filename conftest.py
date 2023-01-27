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


@pytest.fixture
def new_user():
    print("\ncreating user")

    username = uuid.uuid4().__str__().split("-")[-1]
    password = uuid.uuid4().__str__().split("-")[-1]

    url = "https://asperitas.vercel.app/api/register"
    data = {"username": username, "password": password}

    create_user_response = requests.post(url, json=data)

    assert create_user_response.json()["token"] != "", "User not create!"

    return User(username, password)
