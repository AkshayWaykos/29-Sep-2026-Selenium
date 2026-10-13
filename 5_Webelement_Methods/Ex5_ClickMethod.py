import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//button[@class='start']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='stop']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Errorcode 400')]").click()
driver.close()
