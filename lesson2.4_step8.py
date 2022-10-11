#Это версия 2 которая появилась через пару минут.

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    #print (browser.find_element(By.ID, 'price').text)
    
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'),'$100')
    )
    button=browser.find_element(By.ID,'book')
    button.click()
    
    ''' Может и некоректно но думал что сначала нет кнопки или она не кликабельна. 
    WebDriverWait(browser, 5).until(
    #    EC.element_to_be_clickable((By.ID, "solve"))
    #)
    '''
    x=browser.find_element(By.ID,"input_value").text
    an=calc(int(x))
    print(int(x))
    print(an)
    browser.find_element(By.ID, "answer").send_keys(an)
    browser.find_element(By.ID, "solve").click()
    
    

finally:
    time.sleep(15)
    browser.quit()