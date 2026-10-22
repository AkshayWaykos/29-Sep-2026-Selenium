import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)


multipleRows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//td[3]")

for eachRow in multipleRows:
    print(eachRow.text)

time.sleep(5)
driver.close()