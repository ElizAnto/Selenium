from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

"""Взаимодействие с Drop Down"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
"""Первый сайт"""
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
# driver.get(base_url)
# driver.maximize_window()
#
# login_standard_user = "standard_user"
# password_all = "secret_sauce"
#
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# user_name.send_keys(login_standard_user)
# print("Input Login")
#
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print("Input Password")
#
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click Login Button")
#
# select = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
#
# # select.select_by_visible_text('Name (Z to A)')
# select.select_by_value('za')

"""Второй сайт"""
driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
driver.maximize_window()
"""С помощью выбора"""
click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()
print("Click Drop")

click_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[3]")
click_country.click()
print("Click Country")

time.sleep(3)

"""С помощью ввода"""
driver.refresh()
click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()
print("Click Drop")
field = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
field.send_keys("Denmark")
time.sleep(3)
field.send_keys(Keys.RETURN)