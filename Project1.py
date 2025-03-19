from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""SMOKE TESTING"""
"""DELIVERY TWO PRODUCTS"""

"""Work with driver Chrome, work with site for testing"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

"""User login and password"""
login_standard_user = "standard_user"
password_all = "secret_sauce"

"""Input user login and password, input to site with his data"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #data-test XPATH
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

"""INFO Product 1"""
print("INFO Product 1")

product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Add to Cart Product 1")

"""INFO Product 2"""
print("INFO Product 2")

product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print("Add to Cart Product 2")

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter Cart")

"""INFO Cart Product 1"""
print("INFO Cart Product 1")

cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart Product 1 GOOD")

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_product_1 == value_price_cart_product_1
print("INFO Price Cart Product 1 GOOD")

"""INFO Cart Product 2"""
print("INFO Cart Product 2")
cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("INFO Cart Product 2 GOOD")

price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_cart_product_2 = price_cart_product_2.text
print(value_price_cart_product_2)
assert value_price_product_2 == value_price_cart_product_2
print("INFO Price Cart Product 2 GOOD")

"""Click Check Out"""
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Check Out")

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Anton")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Elizarov")
print("Input Last Name")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("123321")
print("Input zip")

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click Continue")

"""INFO Finish Product 1"""
print("INFO Finish Product 1")

finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO Finish Product 1 GOOD")

finish_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO Price Finish Product 1 GOOD")

"""INFO Finish Product 2"""
print("INFO Finish Product 2")

finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("INFO Finish Product 2 GOOD")

finish_price_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = finish_price_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2
print("INFO Price Finish Product 2 GOOD")

"""Summary Price"""
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = ''.join(c if c.isdigit() or c == "." else ' ' for c in summary_price.text).split()
print("Value summary now: " + str(value_summary_price[0]))
total_price_1 = value_finish_price_product_1.lstrip('$')
total_price_2 = value_finish_price_product_2.lstrip('$')
total_price = float(total_price_1) + float(total_price_2)
print("Value summary old: " + str(total_price))
assert total_price == float(value_summary_price[0])
print("Total summary price GOOD")

"""Finish"""
button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
button_finish.click()
print("Click Finish")

finish = driver.find_element(By.XPATH, "//h2[@class='complete-header']")
value_finish = finish.text
print("Find text: " + value_finish)
assert value_finish == "Thank you for your order!"
print("Finish text GOOD")