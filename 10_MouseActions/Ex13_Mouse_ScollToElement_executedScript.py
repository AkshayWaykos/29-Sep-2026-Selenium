import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()

time.sleep(4)
driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,1000)")

time.sleep(5)

driver.execute_script("window.scroll(0,-800)")


time.sleep(10)
driver.close()