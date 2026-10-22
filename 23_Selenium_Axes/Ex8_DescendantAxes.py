import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

#It selects all descendant(children, grandChildren) of  current node.

name=driver.find_element(By.XPATH,"//div[@class='form-group'][1]//descendant::input[1]")
name.send_keys("Akshay")
print(name.get_attribute("value"))

email=driver.find_element(By.XPATH,"//div[@class='form-group'][1]//descendant::input[2]")
email.send_keys("abcd@gmail.com")
print(email.get_attribute("value"))

phone=driver.find_element(By.XPATH,"//div[@class='form-group'][1]//descendant::input[3]")
phone.send_keys("8833774466")
print(phone.get_attribute("value"))

time.sleep(5)
driver.close()