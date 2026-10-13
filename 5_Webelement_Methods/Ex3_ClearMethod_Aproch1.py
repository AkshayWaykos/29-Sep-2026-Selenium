import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Akshay")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name']").clear()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sagar")
driver.close()