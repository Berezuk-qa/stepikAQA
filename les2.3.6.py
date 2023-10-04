from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//button')
    button.click()

    browser.switch_to.window(browser.window_handles[1])
    #new_window = browser.window_handles[1]  #цей код із трьох строк альтернатива одныї строки вище
    #first_window = browser.window_handles[0] #цей код із трьох строк альтернатива одныї строки вище
    #browser.switch_to.window(new_window) #цей код із трьох строк альтернатива одныї строки вище

    import math
    def calc(x):
       return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    sub = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    sub.click()

    print(browser.switch_to.alert.text)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
