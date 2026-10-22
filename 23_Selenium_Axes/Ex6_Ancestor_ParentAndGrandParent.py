import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

#It selects all the ancestor(parent,grandParent) of the current node

ancestor=driver.find_element(By.XPATH,"//input[@id='phone']//ancestor::div[1]")
print(ancestor.get_attribute("class"))
print(ancestor.text)

time.sleep(2)
driver.close()