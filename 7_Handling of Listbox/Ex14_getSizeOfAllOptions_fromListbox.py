import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

allOptiosSize =driver.find_element(By.XPATH,"//select[@id='colors']")

Ops=Select(allOptiosSize)

#APr 1
size=len(Ops.options)
print(size)
print("------------")
#Apr 2
size2=len(Ops.options)
print(size2)
print("------------")
#Apr 3
print(len(Ops.options))

time.sleep(2)
driver.close()