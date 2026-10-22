import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()

time.sleep(4)
driver.get("https://testautomationpractice.blogspot.com/")

act=ActionChains(driver)

act.scroll_by_amount(0,800).perform()

time.sleep(5)

act.scroll_by_amount(0,-600).perform()

time.sleep(10)
driver.close()


