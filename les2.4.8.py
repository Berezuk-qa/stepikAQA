#чекоэмо поки буде ціна 100 потім клікаємо буук, долі обраховуэмо результат та клікаємо кнопку
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element(By.ID, "book")
button.click()

import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

sub = browser.find_element(By.ID, "solve")
sub.click()
print(browser.switch_to.alert.text)

    # закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла

