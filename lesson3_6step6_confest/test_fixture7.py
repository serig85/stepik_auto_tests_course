import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('numb', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
def test_guest_should_see_login_link(browser, numb):
    link = f"https://stepik.org/lesson/{numb}/step/1"
    browser.get(link)


    te=WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ember-text-area")))
    answer = math.log(int(time.time()))
    te.send_keys(answer)
    but=browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    otv=WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    print(otv.text)
    assert otv.text == "Correct!"
    
#,"236897","236898","236899","236903","236904","236905"

#    WebDriverWait(browser, 5).until(
#        EC.visibility_of_element_located(By.CSS_SELECTOR, ".quiz-plugin.ember-view")
#    )


#browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
