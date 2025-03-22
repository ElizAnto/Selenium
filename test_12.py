from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

"""Взаимодействие с iFrame и формой редактирования текста"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
"""Первый сайт"""
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()

"""Первое поле"""
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)
field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]")
value_field = field.text
print(value_field)
time.sleep(3)

field.send_keys(Keys.CONTROL + 'a')
click_editing_panel_bold = driver.find_element(By.XPATH, "//button[@title='Bold']")
click_editing_panel_bold.click()
print("click_editing_panel_bold")
time.sleep(3)

new_field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/b")
value_new_field = new_field.text
print(value_new_field)

assert value_new_field == value_field
print("Редактирование успешно")