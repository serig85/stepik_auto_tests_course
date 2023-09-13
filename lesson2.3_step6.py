def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x=browser.find_element(By.ID, "input_value").text
    an=calc(int(x))
    print(an)
    browser.find_element(By.ID, "answer").send_keys(an)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    
finally:
    time.sleep(5)
    browser.quit()