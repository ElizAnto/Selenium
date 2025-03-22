from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

"""Взаимодействие с формами отправки сообщений и вычислений"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
"""Первый сайт"""
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.maximize_window()

message = 'Hello World'

"""Первое поле"""
input_field = driver.find_element(By.XPATH, "//input[@id='user-message']")
input_field.send_keys(message)
print("Write input_field")
time.sleep(3)

btn1 = driver.find_element(By.XPATH, "//button[@id='showInput']")
btn1.click()
print("Click btn1")
time.sleep(3)

message_field = driver.find_element(By.XPATH, "//p[@id='message']")
value_message_field = message_field.text
print(value_message_field)
assert value_message_field == message
print("GOOD")
time.sleep(3)

"""Второе и третье поле, проверка суммы"""

num_1 = 123
num_2 = 101

input_field_1 = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_field_1.send_keys(str(num_1))
print("Write input_field_1")
time.sleep(3)

input_field_2 = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_field_2.send_keys(str(num_2))
print("Write input_field_2")
time.sleep(3)

btn2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Sum')]")
btn2.click()
print("Click btn2")
time.sleep(3)

summ_field = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_summ_field = summ_field.text
print(value_summ_field)
summer = num_1 + num_2
assert value_summ_field == str(summer)
print("GOOD")