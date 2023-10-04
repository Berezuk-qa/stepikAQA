from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    button = browser.find_element(By.XPATH, '//button[text()="Verify"]').click()
    print(browser.find_element(By.XPATH, '//div[@id="verify_message"]').text)


finally:
    time.sleep(10)
    browser.quit()

