import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Взаимодействие с окнами и вкладками браузера"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.maximize_window()

# """Переключение между вкладками"""
#
# click_tab_button = driver.find_element(By.XPATH, "//button[@id='tabButton']")
# click_tab_button.click()
# print("click_tab_button")
# time.sleep(1)
# print(driver.current_url)
#
# header_1 = driver.find_element(By.XPATH, "//h1[@class='text-center']")
# value_header_1 = header_1.text
# print(value_header_1)
# assert header_1.text == "Browser Windows"
# print("Browser Windows GOOD")
#
# driver.switch_to.window(driver.window_handles[1]) # 1 - индекс вкладки, отсчет от 0
# time.sleep(1)
# print(driver.current_url)
#
# header_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
# value_header_2 = header_2.text
# print(value_header_2)
# assert header_2.text == "This is a sample page"
# print("This is a sample page GOOD")
#
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(1)
# print(driver.current_url)

"""Переключение между окнами"""

click_windows_button = driver.find_element(By.XPATH, "//button[@id='windowButton']")
click_windows_button.click()
print("click_windows_button")
time.sleep(1)
print(driver.current_url)

header_1 = driver.find_element(By.XPATH, "//h1[@class='text-center']")
value_header_1 = header_1.text
print(value_header_1)

windows_1 = driver.window_handles[0]
windows_2 = driver.window_handles[1]

driver.switch_to.window(windows_2)
print(driver.current_url)

header_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
value_header_2 = header_2.text
print(value_header_2)

driver.switch_to.window(windows_1)
print(driver.current_url)
print(value_header_1)