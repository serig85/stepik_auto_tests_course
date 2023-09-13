def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')
    x=browser.find_element(By.ID, "input_value").text
    an=calc(int(x))
    print(an)
    browser.find_element(By.ID, "answer").send_keys(an)
    
    
    button = browser.find_element(By.TAG_NAME,"button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button.click()
    #browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()
