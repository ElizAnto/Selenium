import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Взаимодействие с Check box"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
# https://demoqa.com/buttons
# https://testpages.herokuapp.com/styled/basic-html-form-test.html
base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()

time.sleep(2)
checkbox_1 = driver.find_element(By.XPATH, "//input[@value='cb1']")
checkbox_1.click()
print("Click checkbox_1")

time.sleep(2)
checkbox_3 = driver.find_element(By.XPATH, "//input[@value='cb3']")
checkbox_3.click()
print("Click checkbox_3")

"""Взаимодействие с Radio Button"""

time.sleep(2)
radio_button_1 = driver.find_element(By.XPATH, "//input[@value='rd1']")
radio_button_1.click()
print("Click radio_button_1")

"""Double click (demoqa)"""

time.sleep(2)
action = ActionChains(driver)
double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double).perform() # Метод perform сохраняет результат
print("Double Click button")

"""Right click (demoqa)"""

time.sleep(2)
# action = ActionChains(driver)
right = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right).perform()
print("Right Click button")