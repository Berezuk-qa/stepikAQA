from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration2.html')

    browser.find_element(By.CSS_SELECTOR, "input.first:required").send_keys('Somename')
    browser.find_element(By.CSS_SELECTOR, "input.second:required").send_keys('Somelastname')
    browser.find_element(By.CSS_SELECTOR, "input.third:required").send_keys('Some@email.com')
    browser.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert welcome_text == 'Congratulations! You have successfully registered!'

finally:
    time.sleep(5)

    browser.quit()