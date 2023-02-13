import time
from .base_page import BasePage
from .locators import PostPageLocators
import uuid


class PostPage(BasePage):
    title = uuid.uuid4().__str__().split("-")[-1]
    text = uuid.uuid4().__str__().split("-")[-1]

    def create_text_post(self):
        self.driver.find_element(*PostPageLocators.CREATE_POST_BUTTON).click()
        self.wait_element_to_be_clickable(*PostPageLocators.TEXT_RADIOBUTTON)
        self.driver.find_element(*PostPageLocators.TEXT_RADIOBUTTON).click()
        self.driver.find_element(*PostPageLocators.CATEGORY_SELECTOR).click()
        self.driver.find_element(*PostPageLocators.PROGRAMMING_CATEGORY).click()
        self.driver.find_element(*PostPageLocators.TITLE_FIELD).send_keys(self.title)
        self.driver.find_element(*PostPageLocators.TEXT_FIELD).send_keys(self.text)
        self.driver.find_element(*PostPageLocators.CREATE_POST_BUTTON_IN_FORM).click()
        assert self.is_element_present(*PostPageLocators.TITLE_POST), "Post not created!"

    def delete_post(self):
        self.driver.find_element(*PostPageLocators.USERNAME_IN_HEADER).click()
        self.driver.find_element(*PostPageLocators.TITLE_POST_TEXT).click()
        self.driver.find_element(*PostPageLocators.DELETE_BUTTON).click()
        assert self.is_element_present(*PostPageLocators.EMPTY_POST_LIST_LABEL), "Post not deleted!"

    def create_comment(self):
        self.driver.find_elements(*PostPageLocators.COMMENT_COUNTER)[0].click()
        self.driver.find_element(*PostPageLocators.COMMENT_TEXT_FIELD).send_keys(self.text)
        self.driver.find_element(*PostPageLocators.SUBMIT_BUTTON).click()
        assert self.is_element_present(*PostPageLocators.DELETE_BUTTON), "Comment not created!"

    def delete_comment(self):
        self.driver.find_elements(*PostPageLocators.DELETE_BUTTON)[0].click()
        time.sleep(3)
        assert self.is_element_disappeared(*PostPageLocators.DELETE_BUTTON), "Comment not deleted!"
