from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)
try:
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("email@ya.ru")

    current_dir = os.path.abspath(os.path.dirname("/Users/valeriyavishnevskaya/PycharmProjects/test/Section1_Selenium/lesson6_step11.py"))
    file_path = os.path.join(current_dir, 'lesson6_step11.py')
    file = browser.find_element_by_name("file")
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
