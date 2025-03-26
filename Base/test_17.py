import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Скачивание файла в браузере"""

path_download = "C:\\Users\\Toughie\\PycharmProjects\\Selenium\\files_download"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.maximize_window()

time.sleep(3)
click_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
click_button.click()
print("click_button")
time.sleep(3)

# """Директория не пустая"""
#
# if os.listdir(path_download):
#     print("Файл в наличии")
# else:
#     print("Файла нет")
#
# """Содержимое директории"""
#
# print(os.listdir(path_download))

"""Наличие требуемого файла в директории"""

file_name = "LambdaTest.pdf"

file_path = path_download + "\\" + file_name
assert os.access(file_path, os.F_OK) == True
print("Файл находится в директории")
time.sleep(3)

# """Файл не пуст"""
#
# files = glob.glob(os.path.join(path_download, "*.*")) # *.* - любое расширение
#
# for file in files:
#     a = os.path.getsize(file) # Проверка на размер
#     if a > 10:
#         print("Файл не пуст")
#     else:
#         print("Файл пуст")

"""Очистка директории"""

files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)
print("Файл удален")