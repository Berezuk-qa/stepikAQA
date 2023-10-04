from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

def calc(x):
    return str(str(int(x)+int(y)))

try:
    bro = webdriver.Chrome()
    bro.get(link)

    x_element = bro.find_element(By.CSS_SELECTOR, "[id='num1']")
    x = x_element.text
    y_element = bro.find_element(By.CSS_SELECTOR, "[id='num2']")
    y = y_element.text
    z = calc(x)

    select = Select(bro.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(z)
    bro.find_element(By.TAG_NAME, "button").click()

finally:
    sleep(10)
    bro.quit()