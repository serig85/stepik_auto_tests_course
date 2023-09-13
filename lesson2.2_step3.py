from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects2.html')
    x1=browser.find_element(By.ID, "num1").text
    x2=browser.find_element(By.ID, "num2").text
    y=int(x1)+int(x2)
    print(y)
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(str(y))
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()