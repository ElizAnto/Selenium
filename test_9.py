from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Работа с ползунком"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.schoolsw3.com/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
# click_and_hold - задержать ползунок
# move_by_offset - переместить на X/Y единиц (горизонтально/вертикально)
# release - отпускание мыши
# perform - сохранение
square = driver.find_element(By.XPATH, "//input[@id='id2']") #data-test XPATH
action.click_and_hold(square).move_by_offset(20, 0).release().perform()

print("Square GOOD")
