import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

#In the below XPath expression, it identifies the elements whose single or both conditions are true.

driver.find_element(By.XPATH,"//input[@class='form-control' or @placeholder='Enter Name']").send_keys("Akshay")

time.sleep(5)
driver.close()