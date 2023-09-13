import os
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    browser.find_element(By.NAME, "firstname").send_keys("Billy")
    browser.find_element(By.NAME, "lastname").send_keys("Bond")
    browser.find_element(By.NAME, "email").send_keys("@@@@@")
    browser.find_element(By.NAME, "file").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
finally:
    time.sleep(5)
    browser.quit()