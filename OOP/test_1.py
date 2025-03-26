from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By


class Test_1():
    def test_select_product(self):
        driver = webdriver.Chrome(options=webdriver.ChromeOptions(), service=Service('C:\\Users\\Toughie\\PycharmProjects\\resource\\chromedriver.exe'))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("Start test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")  # data-test XPATH
        user_name.send_keys(login_standard_user)
        print("Input Login")

        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys(password_all)
        print("Input Password")

        button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
        button_login.click()
        print("Click Login Button")

        time.sleep(2)

test = Test_1()
test.test_select_product()