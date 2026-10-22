import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")


#It selects all the nodes that have the same parent as the current node, and appears before the current node.

driver.find_element(By.XPATH,"//input[@id='phone']//preceding-sibling::input[2]").send_keys("Akshay")

time.sleep(2)
driver.close()