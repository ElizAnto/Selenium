# Очистка поля, работа со скрытыми элементами

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #data-test XPATH
user_name.send_keys(login_standard_user)
print("Input Login")
# time.sleep(2)
# user_name.clear()  # Очистка поля user_name

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
print("Click Menu Button")
time.sleep(2)

link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
print("Click Link About Button")

"""Перемещение в истории браузера (вперед-назад)"""
time.sleep(2)
driver.back()
print("Go Back")
time.sleep(2)
driver.forward()
print("Go Forward")