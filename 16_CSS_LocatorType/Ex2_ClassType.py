import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#CSS Locator Type By ID
#driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys("Kiyansh")      #--->by tagname.className
#driver.find_element(By.CSS_SELECTOR,"*.form-control").send_keys("Kiyansh")          #--->by *.className
driver.find_element(By.CSS_SELECTOR,".form-control").send_keys("Kiyansh")      #--->by .name


time.sleep(5)
driver.close()