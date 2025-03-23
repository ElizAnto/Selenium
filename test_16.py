import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Загрузка файла в браузере"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.maximize_window()

path_upload = "C:\\Users\\Toughie\\PycharmProjects\\Selenium\\files_upload\\QA.png"

time.sleep(3)
upload = driver.find_element(By.XPATH, "//input[@id='file']")
upload.send_keys(path_upload)
print("upload")

result_1 = driver.find_element(By.XPATH, "//div[@id='error']")
value_result_1 = result_1.text
print(value_result_1)
assert value_result_1 == "File Successfully Uploaded"
print("GOOD value_result_1")