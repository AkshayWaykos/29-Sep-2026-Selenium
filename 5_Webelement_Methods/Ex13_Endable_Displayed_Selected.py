import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

result1=driver.find_element(By.XPATH,"//button[@class='start']").is_enabled()
print(result1)
if result1:
    print("Is Enabled")
else:
    print("Is Disable")
print("==========================")

result2=driver.find_element(By.XPATH,"//a[contains(text(),'Data Entry Form')]").is_displayed()
print(result2)
if result2:
    print("Is Displayed")
else:
    print("Is Not Displayed")
print("==========================")

driver.find_element(By.XPATH,"//input[@id='sunday']").click()
time.sleep(2)
result3=driver.find_element(By.XPATH,"//input[@id='sunday']").is_selected()
print(result3)
if result3:
    print("Is Selected")
else:
    print("Not Selected")
print("==========================")

