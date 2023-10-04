from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(log(abs(12*sin(int(x)))))
try:
    bro = webdriver.Chrome()
    bro.get(link)

    x = bro.find_element(By.TAG_NAME, "img").get_attribute("valuex")
    y = calc(x)

    bro.find_element(By.ID, "answer").send_keys(y)
    bro.find_element(By.ID, "robotCheckbox").click()
    bro.find_element(By.ID, "robotsRule").click()
    bro.find_element(By.TAG_NAME, "button").click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    sleep(10)
    bro.quit()