import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")


#tag name -- attributes = attributed value with index
#NAME
driver.find_element(By.XPATH,"//input[@class='form-control'][1]").send_keys("Akshay")
#Email
driver.find_element(By.XPATH,"//input[@class='form-control'][2]").send_keys("akki@gmail.com")
#Phone
driver.find_element(By.XPATH,"//input[@class='form-control'][3]").send_keys("7276727847")

time.sleep(5)