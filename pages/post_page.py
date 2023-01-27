from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import uuid


class PostPage(BasePage):

    LOCATOR_CREATE_POST_BUTTON = '//a[contains(@class, "jEpBlT")]'
    LOCATOR_TEXT_BUTTON = '//label[@for="text"]'
    LOCATOR_CATEGORY_SELECTOR = '//select[@name="category"]'
    LOCATOR_PROGRAMMING_CATEGORY = '//option[@value="programming"]'
    LOCATOR_TITLE_FIELD = '//input[@name="title"]'
    LOCATOR_TEXT_FIELD = '//textarea[@name="text"]'
    LOCATOR_CREATE_POST_FORM_BUTTON = '//button[@type="submit"]'

    title = uuid.uuid4().__str__().split("-")[-1]
    text = uuid.uuid4().__str__().split("-")[-1]

    def create_text_post(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.LOCATOR_CREATE_POST_BUTTON).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_TEXT_BUTTON).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_CATEGORY_SELECTOR).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_PROGRAMMING_CATEGORY).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_TITLE_FIELD).send_keys(self.title)
        self.driver.find_element(By.XPATH, self.LOCATOR_TITLE_FIELD).send_keys(self.text)
        self.driver.find_element(By.XPATH, self.LOCATOR_CREATE_POST_FORM_BUTTON).click()

