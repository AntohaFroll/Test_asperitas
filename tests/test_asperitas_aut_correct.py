from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    link = "https://asperitas.vercel.app/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#root > header > a:nth-child(3)").click()
    input1 = browser.find_element(By.NAME, "username")
    input1.send_keys("AntohaFroll")
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("qwerty123456")
    browser.find_element(By.CLASS_NAME, "Button-sc-1mhyaz8-0").click()

finally:
    time.sleep(10)
    browser.quit()