import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""Явное и Неявное ожидание"""

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager' # Позволяет начинать работать со страницей, до того как она загрузится на 100%
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window()

"""Неявное ожидание, распространяется на все действия"""

# driver.implicitly_wait(6)
#
# print("Start test")
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print("Finish test")

"""Явное ожидание, индивидуальное, более стабильное и надежное"""
print("Start test")
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
visible_button.click()
print("Finish test")
