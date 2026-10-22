import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

getColSizeRow=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[3]/td")
print(len(getColSizeRow))

time.sleep(2)
driver.close()