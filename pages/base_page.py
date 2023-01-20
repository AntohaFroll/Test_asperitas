class BasePage:

    url = "https://asperitas.vercel.app/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def go_to(self, url):
        self.driver.get(url)
