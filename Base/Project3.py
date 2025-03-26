from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""SMOKE TESTING"""
"""DELIVERY PRODUCTS TESTING OF YOUR CHOICE"""

"""Choose product"""
print("Приветствую тебя в нашем интернет - магазине")
print("Выбери один из следующих товаров и укажи его номер:\n1 - Sauce Labs Backpack\n2 - Sauce Labs Bike Light\n3 - Sauce Labs Bolt T-Shirt\n4 - Sauce Labs Fleece Jacket\n5 - Sauce Labs Onesie\n6 - Test.allTheThings() T-Shirt (Red)")

number = input()
print("Выбран продукт номер " + number)
link = [4, 0, 1, 5, 2, 3][int(number)-1] # item_title_link

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

"""INFO Product"""
product = driver.find_element(By.XPATH, "//a[@id='item_" + str(link) + "_title_link']")
value_product = product.text
print(value_product)

price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[" + number + "]/div[2]/div[2]/div")
value_price_product = price_product.text
print(value_price_product)

select = "add-to-cart-" + value_product.lower().replace(' ', '-') # Transformation value_product

select_product = driver.find_element(By.XPATH, "//button[@id='" + select + "']")
select_product.click()
print("Select Product " + number)

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter Cart")

"""INFO Cart product"""
cart_product = driver.find_element(By.XPATH, "//a[@id='item_" + str(link) + "_title_link']")
value_cart_product = cart_product.text
print(value_cart_product)
assert value_product == value_cart_product
print("INFO Cart Product " + number + " GOOD")

price_cart_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product = price_cart_product.text
print(value_price_cart_product)
assert value_price_product == value_price_cart_product
print("INFO Price Cart Product " + number + " GOOD")

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Check Out")

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Alex")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Ivanov")
print("Input Last Name")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("123321")
print("Input zip")

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click Continue")

"""INFO Finish product"""
finish_product = driver.find_element(By.XPATH, "//a[@id='item_" + str(link) + "_title_link']")
value_finish_product = finish_product.text
print(value_finish_product)
assert value_product == value_finish_product
print("INFO Finish Product " + number + " GOOD")

finish_price_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product = finish_price_product.text
print(value_finish_price_product)
assert value_price_product == value_finish_price_product
print("INFO Price Finish Product " + number + " GOOD")

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + value_finish_price_product
print(item_total)
assert value_summary_price == item_total
print("Total summary price GOOD")

button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
button_finish.click()
print("Click Finish")

finish = driver.find_element(By.XPATH, "//h2[@class='complete-header']")
value_finish = finish.text
print(value_finish)
assert value_finish == "Thank you for your order!"
print("Finish text GOOD")