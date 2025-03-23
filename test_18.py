import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Отработка исключений"""

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager' # Позволяет начинать работать со страницей, до того как она загрузится на 100%
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
# base_url = 'https://demoqa.com/dynamic-properties' # 1
base_url = 'https://demoqa.com/radio-button' # 2
driver.get(base_url)
driver.maximize_window()

"""url #1"""

# try:
#     visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     visible_button.click()
# except NoSuchElementException as exception:
#     print("NoSuchElementException exception")
#     time.sleep(6)
#     visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     visible_button.click()
#     print("Click visible_button")

"""Radio Button (url#2)"""
yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_checkbox.click()
try:
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "No"
except AssertionError as exception:
    driver.refresh()
    # time.sleep(3)
    yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_checkbox.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
    print("CheckBox Yes")
print("Test over")