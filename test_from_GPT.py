import unittest
from selenium import webdriver

class TestRegistration1(unittest.TestCase):
    def setUp(self):
        # Инициализация веб-драйвера
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Закрытие браузера после выполнения теста
        self.driver.quit()

    def test_registration1(self):
        # Открытие страницы http://suninjuly.github.io/registration1.html
        self.driver.get("http://suninjuly.github.io/registration1.html")

        # Находим элементы формы и заполняем их
        self.driver.find_element_by_css_selector(".first_block .first").send_keys("Имя")
        self.driver.find_element_by_css_selector(".first_block .second").send_keys("Фамилия")
        self.driver.find_element_by_css_selector(".first_block .third").send_keys("Email")

        # Нажимаем на кнопку "Отправить"
        self.driver.find_element_by_css_selector("button.btn").click()

        # Проверяем, что после отправки формы появляется сообщение об успешной регистрации
        success_message = self.driver.find_element_by_tag_name("h1").text
        self.assertEqual(success_message, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
