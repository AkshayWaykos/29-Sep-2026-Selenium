import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)


multipleData=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[position()=3 or position()=7]/td[4]")

for eachData in multipleData:
    print(eachData.text)


time.sleep(4)
driver.close()