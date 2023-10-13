from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest

link = "https://stepik.org/lesson/236895/step/1"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(5)
    sub = browser.find_element(By.ID, 'ember33')
    sub.click()

    emai = browser.find_element(By.ID, 'id_login_email')
    emai.send_keys("Ivan")
    passw = browser.find_element(By.ID, 'id_login_password')
    passw.send_keys("Petrov")

    button = browser.find_element(By.XPATH, '//button[text()="Войти"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла