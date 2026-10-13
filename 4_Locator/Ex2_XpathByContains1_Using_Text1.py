import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

#click on link - Hidden Elements & AJAX
driver.find_element(By.XPATH,"//a[contains(text(),'AJAX')]").click()


time.sleep(2)
