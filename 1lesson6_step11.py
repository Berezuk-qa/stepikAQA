from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"#link = "http://suninjuly.github.io/registration1.html -- тут неповинен падати"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    Inp_Name = browser.find_element(By.XPATH, '//label[text()="First name*"]/../input')
    Inp_Name.send_keys("Gbljh")
    Inp_Last_Name = browser.find_element(By.XPATH, '//label[text()="Last name*"]/../input')
    Inp_Last_Name.send_keys("Ujdyj")
    Inp_Email = browser.find_element(By.XPATH, '//label[text()="Email*"]/../input')
    Inp_Email.send_keys("Gbljh@Ujdyj.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
