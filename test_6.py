# Smoking test

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
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

"""INFO Product #1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter Cart")

"""INFO Cart product 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart product 1 GOOD")

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_product_1 == value_price_cart_product_1
print("INFO Price Cart product 1 GOOD")

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Check Out")

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Alex")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Ivanov")
print("Click Check Out")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("1234")
print("Click Check Out")

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click Continue")

"""INFO Finish product 1"""
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO Finish product 1 GOOD")

finish_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO Price Finish product 1 GOOD")

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + value_finish_price_product_1
print(item_total)
assert value_summary_price == item_total
print("Total summary price GOOD")