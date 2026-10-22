import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#first-of-type
driver.find_element(By.CSS_SELECTOR,"input[class=form-control]:first-of-type").send_keys("Akshay")


#nth-of-type(2)
driver.find_element(By.CSS_SELECTOR,"input[class=form-control]:nth-of-type(2)").send_keys("Akshay@gmail.com")

#last-of-type
driver.find_element(By.CSS_SELECTOR,"input[class=form-control]:last-of-type").send_keys("991122883388")

time.sleep(2)
driver.close()