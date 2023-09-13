def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

import math
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x=browser.find_element(By.ID, "input_value").text
    an=calc(int(x))
    print(an)
    browser.find_element(By.ID, "answer").send_keys(an)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    
    
finally:
    time.sleep(5)
    browser.quit()