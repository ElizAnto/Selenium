from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from faker import Faker
from selenium.webdriver.common.by import By

"""Генерирование случайных данных с библиотекой Faker"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# faker = Faker("ru_RU")
faker = Faker("en_US")

name = faker.first_name() + str(faker.random_int())
print(name)
passw = faker.password()
print(passw)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #data-test XPATH
user_name.send_keys(name)
print("Input Login")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(passw)
print("Input Password")