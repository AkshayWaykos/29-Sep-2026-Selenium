import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

#driver.find_element(By.XPATH,"//input[@id='male']").click()        #click on radio button

result=driver.find_element(By.XPATH,"//input[@id='male']").is_selected()
print(result)

if result:
    print("Is Selected")
else:
    print("Is not selected")

driver.close()

