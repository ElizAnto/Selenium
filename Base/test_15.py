import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Взаимодействие с предупреждениями и всплывающими уведомлениями"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.maximize_window()

"""Предупреждение с кнопкой ОК"""

click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
click_alert_button.click()
print("click_alert_button")
time.sleep(3)
driver.switch_to.alert.accept()

result_1 = driver.find_element(By.XPATH, "//p[@id='result']")
value_result_1 = result_1.text
print(value_result_1)
assert value_result_1 == "You successfully clicked an alert"
print("GOOD value_result_1")

"""Предупреждение с кнопками ОК и отмена"""

click_confirm_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
click_confirm_button.click()
print("click_confirm_button")
time.sleep(3)
driver.switch_to.alert.accept()

result_2 = driver.find_element(By.XPATH, "//p[@id='result']")
value_result_2 = result_2.text
print(value_result_2)
assert value_result_2 == "You clicked: Ok"
print("GOOD value_result_2")

click_confirm_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
click_confirm_button.click()
print("click_confirm_button")
time.sleep(3)
driver.switch_to.alert.dismiss()

result_3 = driver.find_element(By.XPATH, "//p[@id='result']")
value_result_3 = result_3.text
print(value_result_3)
assert value_result_3 == "You clicked: Cancel"
print("GOOD value_result_3")
