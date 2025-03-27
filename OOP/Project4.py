from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
password = 'secret_sauce'

"""Test login of all users"""

class Test():

    """Ввод логина и пароля"""
    def login(self, login_name, login_password):

        user_name = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print("Input Login")

        pass_word = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        pass_word.send_keys(login_password)
        print("Input Password")

    """Вход в систему"""
    def authorisation(self):

            button_login = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
            button_login.click()
            print("Click Login Button")

            # Проверяем, что нет сообщения об ошибке
            try:
                check_error = WebDriverWait(driver, 0.5).until(
                    EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))

                # Если ошибка появилась
                value_check_error = check_error.text
                print(f"Found error: {value_check_error}")
                if value_check_error == 'Epic sadface: Sorry, this user has been locked out.':
                    print("User is locked out, refreshing page")
                    driver.refresh()
                    return False
            except:
                # Если ошибки нет - проверка, что находимся на сайте
                success_test = WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
                value_success_test = success_test.text
                assert value_success_test == 'Products'
                print("Test Success!")
                return True

    """Выход из системы"""
    def logout(self):

        button_menu = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        button_menu.click()
        print("Click Menu")

        button_logout = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        button_logout.click()
        print("Click Logout Button")

"""Открытие сайта"""
driver = webdriver.Chrome(options=webdriver.ChromeOptions(), service=Service('C:\\Users\\Toughie\\PycharmProjects\\resource\\chromedriver.exe'))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

print("START TEST")

test = Test()

"""Тест каждого пользователя"""
for i in usernames:
    print("Тест пользователя: " + i)
    test.login(i, password)
    flag = test.authorisation()
    if flag:
        test.logout()
    else:
        continue

print("END TEST")