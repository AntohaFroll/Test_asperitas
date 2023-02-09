import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid


class PostPage(BasePage):
    title = uuid.uuid4().__str__().split("-")[-1]
    text = uuid.uuid4().__str__().split("-")[-1]

    LOCATOR_CREATE_POST_BUTTON = '//a[contains(@class, "exvOBC")]'
    LOCATOR_TEXT_RADIOBUTTON = '//label[@for="text"]'
    LOCATOR_CATEGORY_SELECTOR = '//select[@name="category"]'
    LOCATOR_PROGRAMMING_CATEGORY = '//option[@value="programming"]'
    LOCATOR_TITLE_FIELD = '//input[@name="title"]'
    LOCATOR_TEXT_FIELD = '//textarea[@name="text"]'
    LOCATOR_CREATE_POST_FORM_BUTTON = '//button[@type="submit"]'
    LOCATOR_TITLE_POST = '//div[contains(@class, "Title__Wrapper")]'
    LOCATOR_HEADER_USERNAME = '//span[contains(@class, "HeaderUsernameText")]'
    LOCATOR_DELETE_BUTTON = '//button[contains(@class, "DeleteButton")]'
    LOCATOR_EMPTY_POST_LIST_LABEL = '//div[contains(@class, "Empty__Wrapper")]'
    LOCATOR_TITLE_POST_TEXT = '//div[contains(@class, "Title__Wrapper")]/a'
    LOCATOR_COMMENT_TEXT_FIELD = '//textarea[@name="comment"]'
    LOCATOR_SUBMIT_BUTTON = '//button[@type="submit"]'
    LOCATOR_CREATED_COMMENT = f'//p[text()="{text}"]'
    LOCATOR_COMMENT_COUNTER = '//div[contains(@class, "Detail__Wrapper")]/a'

    def create_text_post(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_CREATE_POST_BUTTON).click()
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.LOCATOR_TEXT_RADIOBUTTON))).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_CATEGORY_SELECTOR).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_PROGRAMMING_CATEGORY).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_TITLE_FIELD).send_keys(self.title)
        self.driver.find_element(By.XPATH, self.LOCATOR_TEXT_FIELD).send_keys(self.text)
        self.driver.find_element(By.XPATH, self.LOCATOR_CREATE_POST_FORM_BUTTON).click()
        assert len(self.driver.find_elements(By.XPATH, self.LOCATOR_TITLE_POST)) == 1,\
            "Post not created!"

    def delete_post(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_HEADER_USERNAME).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_TITLE_POST_TEXT).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_DELETE_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATOR_EMPTY_POST_LIST_LABEL)),
            "Post not deleted!")

    def create_comment(self):
        self.driver.implicitly_wait(5)
        self.driver.find_elements(By.XPATH, self.LOCATOR_COMMENT_COUNTER)[0].click()
        self.driver.find_element(By.XPATH, self.LOCATOR_COMMENT_TEXT_FIELD).send_keys(self.text)
        self.driver.find_element(By.XPATH, self.LOCATOR_SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.LOCATOR_CREATED_COMMENT), self.text),
            "Comment not deleted!")

    def delete_comment(self):
        self.driver.implicitly_wait(5)
        self.driver.find_elements(By.XPATH, self.LOCATOR_DELETE_BUTTON)[0].click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.LOCATOR_CREATED_COMMENT)),
            "Comment not deleted!")
