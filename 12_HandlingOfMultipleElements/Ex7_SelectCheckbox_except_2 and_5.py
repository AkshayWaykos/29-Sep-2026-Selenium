#2: Select all checkboxes except 2nd & 5th.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,2700)")

checkBox=driver.find_elements(By.XPATH,"//table[@id='productTable']//input[@type='checkbox']")

count=1
for eachCheckbox in checkBox:
    if count!=2 and count!=5:
        eachCheckbox.click()
        time.sleep(2)
    count += 1

time.sleep(10)
driver.close()