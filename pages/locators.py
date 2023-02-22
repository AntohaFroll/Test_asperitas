from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, "//a[text()='asperitas']")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    SIGNUP_LINK = (By.XPATH, "//a[@href='/signup']")
    CREATE_POST_LINK = (By.XPATH, "//a[contains(@class, 'exvOBC')]")
    USERNAME_LINK = (By.XPATH, "//span[contains(@class, 'HeaderUsernameText')]")


class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    MESSAGE_REQUIRED = (By.XPATH, "//span[text()='required']")
    MESSAGE_CONTAINS_INVALID_CHARACTERS = (By.XPATH, "//span[text()='contains invalid characters']")
    MESSAGE_MUST_BE_MORE_THAN_8_CHARACTERS = (By.XPATH, "//span[text()='must be more than 8 characters']")
    MESSAGE_INVALID_PASSWORD = (By.XPATH, "//div[text()='invalid password']")


class SignupPageLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@name='password2']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@type='submit']")
    MESSAGE_REQUIRED = (By.XPATH, "//span[text()='required']")
    MESSAGE_CONTAINS_INVALID_CHARACTERS = (By.XPATH, "//span[text()='contains invalid characters']")
    MESSAGE_MUST_BE_MORE_THAN_8_CHARACTERS = (By.XPATH, "//span[text()='must be more than 8 characters']")
    MESSAGE_PASSWORD_MUST_MATCH = (By.XPATH, "//span[text()='passwords must match']")
    CREATE_POST_BUTTON = (By.XPATH, "//a[contains(@class, 'jEpBlT')]")


class PostPageLocators:
    TEXT_RADIOBUTTON = (By.XPATH, "//label[@for='text']")
    URL_RADIOBUTTON = (By.XPATH, "//label[@for='link']")
    CATEGORY_SELECTOR = (By.XPATH, "//select[@name='category']")
    PROGRAMMING_CATEGORY = (By.XPATH, "//option[@value='programming']")
    TITLE_FIELD = (By.XPATH, "//input[@name='title']")
    TEXT_FIELD = (By.XPATH, "//textarea[@name='text']")
    URL_FIELD = (By.XPATH, "//input[@name='url']")
    CREATE_POST_BUTTON = (By.XPATH, "//button[@type='submit']")
    TITLE_POST = (By.XPATH, "//div[contains(@class, 'Title__Wrapper')]")
    DELETE_BUTTON = (By.XPATH, "//button[contains(@class, 'DeleteButton')]")
    EMPTY_POST_LIST_LABEL = (By.XPATH, "//div[contains(@class, 'Empty__Wrapper')]")
    TITLE_POST_TEXT = (By.XPATH, "//div[contains(@class, 'Title__Wrapper')]/a")
    COMMENT_TEXT_FIELD = (By.XPATH, "//textarea[@name='comment']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    COMMENT_COUNTER = (By.XPATH, '//div[contains(@class, "Detail__Wrapper")]/a[text()=" comment"]')
