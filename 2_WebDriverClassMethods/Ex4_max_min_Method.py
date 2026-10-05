print("==WebDriver Method Max and Min Method==")
import time
from selenium import webdriver

driver=webdriver.Firefox()
time.sleep(5)
driver.get('https://www.google.com/')
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()

driver.close()

