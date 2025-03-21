import time
import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Работа с календарем, выбор даты через 10 дней от настоящей даты"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

"""Очистка поля с датой"""
new_date.click()
new_date.send_keys(Keys.CONTROL + "a")
new_date.send_keys(Keys.BACKSPACE)

"""Сегодняшняя дата"""
now_date = datetime.datetime.now()
print("Сегодняшняя дата: " + str(now_date.strftime('%Y-%m-%d')))

"""Дата через 10 дней"""
future_date = now_date + datetime.timedelta(days=10)
print("Дата через 10 дней: " + str(future_date.strftime('%Y-%m-%d')))

"""Необходимая информация о дате через 10 дней"""
day_week = future_date.strftime('%A')  # Полное название дня недели
month = future_date.strftime('%B')  # Полное название месяца
day = int(future_date.strftime('%d'))
year = future_date.strftime('%Y')
# Окончание дня месяца (st, nd, rd, th)
if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = 'th'
else:
    suffix = ['st', 'nd', 'rd'][day % 10 - 1]

locator = "//div[@aria-label='Choose " + str(day_week) + ", " + str(month) + " " + str(day) + suffix + ", " + year + "']"
print("Локатор: " + locator)

"""Выбор даты"""
new_date.click()
time.sleep(2)
tomorrow = driver.find_element(By.XPATH, locator)
tomorrow.click()

print("GOOD")
