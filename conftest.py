import pytest
from selenium import webdriver
import requests
import uuid
from entities.user import User
from entities.post import Post

reg_url = "https://asperitas.vercel.app/api/register"
auth_url = "https://asperitas.vercel.app/api/login"
post_url = "https://asperitas.vercel.app/api/posts"


@pytest.fixture
def driver():
    print("\nStart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nQuit browser")
    driver.quit()


@pytest.fixture
def new_user():
    print("\nCreating user")
    username = uuid.uuid4().__str__().split("-")[-1]
    password = uuid.uuid4().__str__().split("-")[-1]
    data = {"username": username, "password": password}
    create_user_response = requests.post(reg_url, json=data)
    user_token = create_user_response.json()["token"]
    assert user_token != "", "User not create"
    return User(username, password, user_token)


@pytest.fixture
def new_post(new_user):
    print("\nCreating new post")
    title = uuid.uuid4().__str__().split("-")[-1]
    text = uuid.uuid4().__str__().split("-")[-1]
    data = {"category": "music", "type": "text", "title": title, "text": text}
    authorization = {"authorization": f"Bearer {new_user.user_token}"}
    create_post_response = requests.post(post_url, json=data, headers=authorization)
    assert create_post_response.json() != "", "Post not create"
    return Post(title, text)


@pytest.fixture
def generate_unique_string():
    unique_string = uuid.uuid4().__str__().split("-")[-1]
    return unique_string


@pytest.fixture
def generate_url():
    unique_url = f"http://{uuid.uuid4().__str__().split('-')[-1]}.com"
    return unique_url


@pytest.fixture
def generate_password():
    password = uuid.uuid1().__str__().split("-")[-1]
    return password


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
