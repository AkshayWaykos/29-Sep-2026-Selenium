import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,2700)")

checkBox=driver.find_elements(By.XPATH,"//table[@id='productTable']//input[@type='checkbox']")

#select check box from table.
for eachCheckBox in checkBox:
    time.sleep(2)
    eachCheckBox.click()

#deSelect checkBox from table
time.sleep(5)
for eachCheckBox in checkBox:
    time.sleep(2)
    eachCheckBox.click()

time.sleep(5)
driver.close()

