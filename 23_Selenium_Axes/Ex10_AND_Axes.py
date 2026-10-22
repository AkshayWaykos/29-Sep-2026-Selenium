import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

#expression, two conditions are used, both conditions should be true to find the element.
#It fails to find an element if any one condition is false.

driver.find_element(By.XPATH,"//input[@class='form-control' and @placeholder='Enter Name']").send_keys("Akshay")


time.sleep(5)
driver.close()
