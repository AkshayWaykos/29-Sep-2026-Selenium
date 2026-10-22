import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get(" https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,500)")

time.sleep(5)

#reference days and select sibling checkboxes.
allDays=driver.find_elements(By.XPATH,"//div[@class='form-group'][4]//following-sibling::input[1]")

for eachDays in allDays:
    eachDays.click()
    time.sleep(1)

time.sleep(2)
driver.close()
