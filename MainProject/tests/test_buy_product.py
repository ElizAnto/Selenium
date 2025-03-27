from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from MainProject.pages.login_page import LoginPage


def test_buy_product():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions(),
                              service=Service('C:\\Users\\Toughie\\PycharmProjects\\resource\\chromedriver.exe'))

    print("Start test")

    login = LoginPage(driver)
    login.authorisation()

    enter_shopping_cart = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    enter_shopping_cart.click()
    print("Click Enter Shopping Cart")

    time.sleep(2)