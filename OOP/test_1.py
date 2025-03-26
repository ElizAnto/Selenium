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

        time.sleep(2)

test = Test_1()
test.test_select_product()