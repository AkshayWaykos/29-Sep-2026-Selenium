import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

#It selects all the direct children of  current node.

driver.find_element(By.XPATH,"(//div[@class='form-group'])[1]//child::input[1]").send_keys("Akshay")
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='form-group'])[1]//child::input[2]").send_keys("abcd@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='form-group'])[1]//child::input[3]").send_keys("9922883377")
time.sleep(5)

driver.close()