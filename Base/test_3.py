# KEYBOARD

import time, datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless") # Не открывать браузер
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #data-test XPATH
user_name.send_keys(login_standard_user)
print("Input Login")
# # Стереть и добавить символы в строку
# time.sleep(2)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# user_name.send_keys("er")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

user_name.send_keys(Keys.RETURN) # Нажатие на клавишу ENTER, минуя кнопку Login
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click Login Button")

filter = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']")
filter.click()
print("Click filter")
time.sleep(2)
filter.send_keys(Keys.DOWN) # Кнопка на клавиатуре вниз
time.sleep(2)
filter.send_keys(Keys.RETURN)
# Скрин
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screenshot = "screenshot " + now_date + ".png"
# ./Screen - точка указывает на текущий каталог, то есть найти в этом проекте папку Screen
driver.save_screenshot(f".//Screen//{name_screenshot}")
print("Screenshot done")