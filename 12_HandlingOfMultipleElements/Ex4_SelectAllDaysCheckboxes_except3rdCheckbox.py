import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,500)")

allCheckboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
print(len(allCheckboxes))

count=1
for eachCheckboxes in allCheckboxes:
    if count!=4 and count!=6:
        eachCheckboxes.click()
        time.sleep(2)
    count+=1

time.sleep(2)
driver.close()
