from selenium.webdriver.common.by import By


class BasePage:

    url = "https://asperitas.vercel.app/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def go_to(self, url):
        self.driver.get(url)

    def should_page_open(self):
        logo = self.driver.find_elements(By.XPATH, '//a[text()="asperitas"]')
        assert len(logo) == 1, "Page don't open!"
