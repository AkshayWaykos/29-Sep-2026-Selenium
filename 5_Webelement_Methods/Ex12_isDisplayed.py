import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

result=driver.find_element(By.XPATH,"//a[contains(text(),'Data Entry Form')]").is_displayed()
print(result)

if result:
    print("Is Displayed")
else:
    print("Is Not Displayed")
