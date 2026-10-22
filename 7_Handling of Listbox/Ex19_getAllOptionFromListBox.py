import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

completedOptions=driver.find_element(By.XPATH,"//select[@id='colors']")

cl=Select(completedOptions)

showAll=cl.options

for eachOption in showAll:
    print("Color from list =",eachOption.text)

print("===========================")

showSize=cl.options
size=len(showSize)
print("Total option size from list =",size)

time.sleep(2)
driver.close()