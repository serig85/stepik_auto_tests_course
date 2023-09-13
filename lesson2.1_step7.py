def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x=browser.find_element(By.ID, "treasure").get_attribute("valuex")
    an=calc(int(x))
    print(an)
    browser.find_element(By.ID, "answer").send_keys(an)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()