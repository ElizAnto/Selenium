import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Работа с календарем"""
def field_clear(new_date):
    new_date.click()
    new_date.send_keys(Keys.CONTROL + "a")
    new_date.send_keys(Keys.BACKSPACE)
    return

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

# """Копирование даты в поле"""
# field_clear(new_date)
# time.sleep(2)

# new_date.click()
# time.sleep(2)
# new_date.send_keys("06/07/2022")
# time.sleep(2)
# new_date.send_keys(Keys.RETURN)
# time.sleep(2)
#
# """Выбор даты кликом мыши по кнопке"""
# field_clear(new_date)
# time.sleep(2)

# new_date.click()
# time.sleep(2)
# date = driver.find_element(By.XPATH, "//div[@aria-label='Choose Wednesday, June 8th, 2022']")
# date.click()

# time.sleep(2)

"""Сегодняшний день"""
field_clear(new_date)
time.sleep(2)

new_date.click()
time.sleep(2)
today = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")
today.click()

time.sleep(2)

"""Завтрашний день"""

field_clear(new_date)
time.sleep(2)

now_date = datetime.datetime.now().strftime("%d")
print(now_date)
tomorrow_date = int(now_date) + 1
locator = "//div[@aria-label='Choose Saturday, March " + str(tomorrow_date) + "nd, 2025']"
print(locator)

new_date.click()
time.sleep(2)
tomorrow = driver.find_element(By.XPATH, locator)
tomorrow.click()
print("GOOD")
