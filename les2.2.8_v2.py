from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    selector = ["[name = 'firstname']", "[name='lastname']", "[name='email']", "[name='file']"]
    answers = ['first_name', 'second_name', 'e_mail@mail.ru',file_path]

    for k, v in enumerate(selector):
        browser.find_element(By.CSS_SELECTOR, v).send_keys(answers[k])

    submit_button=browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(5)
    browser.quit()