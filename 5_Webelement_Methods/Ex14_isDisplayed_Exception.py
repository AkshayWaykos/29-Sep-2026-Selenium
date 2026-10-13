import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

try:
    result=driver.find_element(By.XPATH,"//a[contains(text(),'Data Entry FORM')]").is_displayed()
except NoSuchElementException:
    result=False
    print("Exception handled: Element not found")
    print(result)

if result:
    print("Element is Displayed")
else:
    print("Element is not Displayed")

time.sleep(5)