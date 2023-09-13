import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html" #Без ошибки
        #link = "http://suninjuly.github.io/registration2.html" #С ошибкой  Во втором блоке тоже есть second и в 1 и во втором случае надо указывать блок!!!
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.second') #Без указания блока 2 вариант попадает в "Address"
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.third')
        input3.send_keys("Smolensk@@")
    
            # Отправляем заполненную форму
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text)

    def test_abs2(self):
        #link = "http://suninjuly.github.io/registration1.html" #Без ошибки
        link = "http://suninjuly.github.io/registration2.html" #С ошибкой  Во втором блоке тоже есть second и в 1 и во втором случае надо указывать блок!!!
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.second') #Без указания блока 2 вариант попадает в "Address"
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR,'.first_block .form-control.third')
        input3.send_keys("Smolensk@@")
    
            # Отправляем заполненную форму
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find(By.TAG_NAME,"h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text)


        
        
if __name__ == "__main__":
    unittest.main()

# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()
