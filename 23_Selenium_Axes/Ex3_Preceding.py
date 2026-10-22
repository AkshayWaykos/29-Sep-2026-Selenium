import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")

#Select all the nodes that appear before the current node(phone).
allPreceding=driver.find_elements(By.XPATH, "//input[@id='phone']//preceding::a")

for eachPreceding in allPreceding:
    print(eachPreceding.text)
    time.sleep(1)

time.sleep(4)
driver.close()

