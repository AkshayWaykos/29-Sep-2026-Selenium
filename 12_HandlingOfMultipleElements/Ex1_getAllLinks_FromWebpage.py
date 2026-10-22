import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

allLink=driver.find_elements(By.XPATH,"//a")

print(len(allLink))

for eachLink in allLink:
    print(eachLink.text)

time.sleep(4)
driver.close()
