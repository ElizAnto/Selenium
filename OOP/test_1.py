from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from OOP.login_page import LoginPage


class Test_1():
    def test_select_product(self):
        driver = webdriver.Chrome(options=webdriver.ChromeOptions(), service=Service('C:\\Users\\Toughie\\PycharmProjects\\resource\\chromedriver.exe'))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("Start test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        login = LoginPage(driver)
        login.authorisation(login_standard_user, password_all)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click Select Product")

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        enter_shopping_cart.click()
        print("Clock Enter Shopping Cart")

        success_test = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print("Test Success!")

        time.sleep(2)

test = Test_1()
test.test_select_product()