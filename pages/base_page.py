class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://asperitas.vercel.app/"

    def open(self):
        self.driver.get(self.url)
