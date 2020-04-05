from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    x =x_element.text
    # plus_element = browser.find_element_by_css_selector("span:nth-child(3)")
    # plus = plus_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    sum1 = str(int(x)+int(y))
    # browser.find_element_by_tag_name("select").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)

    browser.quit()
