import time
from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

result=driver.find_element(By.XPATH,"//button[@class='start']").is_enabled()
print(result)

if result:
    print("Button is Enabled")
else:
    print("Button is Not Enabled")