import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

#It selects parent of the current node

driver.find_element(By.XPATH,"//input[@id='phone']//parent::div//input[3]").send_keys("9933884477")

time.sleep(5)
driver.close()