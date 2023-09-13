import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


print("\nstart browser for test..")
browser = webdriver.Chrome()

link = f"https://stepik.org/lesson/236895/step/1"
browser.get(link)

te=WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ember-text-area")))
answer = math.log(int(time.time()))
te.send_keys(answer)
but=browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

otv=WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
print(otv.text)

time.sleep(10)
#el=browser.find_element(By.CSS_SELECTOR, ".submit-submission")
#el.send_keys("abc")
#time.sleep(3)
print("\nquit browser..")
browser.quit()
