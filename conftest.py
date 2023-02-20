import pytest
from selenium import webdriver
import requests
import uuid
# TODO зачем тебе UserAuthorized? Это же копия User...
from entities.user import User, UserAuthorized


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

    # TODO url надо выносить наверх файла, в константы
    url = "https://asperitas.vercel.app/api/register"
    data = {"username": username, "password": password}

    create_user_response = requests.post(url, json=data)

    assert create_user_response.json()["token"] != "", "User not create!"

    return User(username, password)


# TODO generate_username и generate_password не отличаются, соответственно,
# TODO можно просто сделать одну фикстуру generate_unique_string
@pytest.fixture
def generate_username():
    username = uuid.uuid4().__str__().split("-")[-1]

    return username


@pytest.fixture
def generate_password():
    password = uuid.uuid1().__str__().split("-")[-1]

    return password

# TODO зачем это, если везде можно просто вставлять "Hello world"?
@pytest.fixture
def generate_text():
    text = uuid.uuid4().__str__().split("-")[-1]

    return text


# @pytest.fixture
# def user_authorized():
#     print("\ncreating and authorization user")
#
#     username = uuid.uuid4().__str__().split("-")[-1]
#     password = uuid.uuid4().__str__().split("-")[-1]
#
#     reg_url = "https://asperitas.vercel.app/api/register"
#     auth_url = "https://asperitas.vercel.app/api/login"
#     data = {"username": username, "password": password}
#
#     create_user_response = requests.post(reg_url, json=data)
#
#     assert create_user_response.json()["token"] != "", "User not created!"
#
#     authorization_user_response = requests.post(auth_url, json=data)
#
#     assert authorization_user_response.json()["token"] != "", "User not authorized!"
#
#     return UserAuthorized(username, password)
