import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#CSS Locator Type By ID
#driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("Kiyansh")      #--->by tagname#name
#driver.find_element(By.CSS_SELECTOR,"*#name").send_keys("Kiyansh")          #--->by *name
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Kiyansh")      #--->by #name


time.sleep(5)
driver.close()