from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1=browser.find_element_by_id('num1')
    x=element1.text
    element2=browser.find_element_by_id('num2')
    y=element2.text
    summa=str(int(x)+int(y))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(summa)

    button=browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
