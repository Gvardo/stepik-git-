from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
# импорт нужных бтблиотек 
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
import os
import time

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"    
    browser = webdriver.Chrome()
    browser.get(link)
    
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button1 = browser.find_element_by_id('book')
    button1.click()
    # assert "successful" in message.text

    input1 = browser.find_element_by_id('input_value')
    x = input1.text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    
    button2 = browser.find_element_by_id('solve') #browser.find_element_by_css_selector('button.btn')
    button2.click()
    
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()