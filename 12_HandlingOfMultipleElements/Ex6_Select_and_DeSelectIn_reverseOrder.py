import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,2700)")

#click on 2 no tab of WebTable.
driver.find_element(By.XPATH,"(//a[@href='#'])[2]").click()

time.sleep(5)
selectCheckBox=driver.find_elements(By.XPATH,"//table[@id='productTable']//input[@type='checkbox']")

#select in Forward Direction.
for eachCheckBox in selectCheckBox:
    eachCheckBox.click()
    time.sleep(2)

time.sleep(5)

#De-select in Reverse Direction.
for eachCheckBox in reversed(selectCheckBox):
    eachCheckBox.click()
    time.sleep(2)


time.sleep(10)
driver.close()