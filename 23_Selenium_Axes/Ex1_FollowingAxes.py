import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

time.sleep(5)

#refer Name and enter phone no details with the help of following Axes
driver.find_element(By.XPATH,"//label[text()='Name:']//following::input[@id='phone']").send_keys("9922883377")

time.sleep(5)
driver.close()