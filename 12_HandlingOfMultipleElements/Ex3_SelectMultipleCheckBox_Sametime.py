import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,500)")

allCheckboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
print(len(allCheckboxes))

#select all check Box
for eachCheckBox in allCheckboxes:
    eachCheckBox.click()
    time.sleep(2)

#Deselect all check box with same logic
for eachCheckBox in allCheckboxes:
    eachCheckBox.click()
    time.sleep(2)

time.sleep(5)
driver.close()
