import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,500)")

checkBox=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
print(len(checkBox))

for eachBox in checkBox:
    eachBox.click()
    time.sleep(1)

for eachBox in reversed(checkBox):
    eachBox.click()
    time.sleep(1)

count=1
for eachBox in checkBox:
    if count!=2 and count!=4:
        eachBox.click()
        time.sleep(1)

time.sleep(1)
driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\12_HandlingOfMultipleElements\\SaveScreen\\SS_01.png")

time.sleep(1)
driver.close()
