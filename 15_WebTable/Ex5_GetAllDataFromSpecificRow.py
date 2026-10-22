import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)


multipleCols1=driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr[2]/td")

for eachCol1 in multipleCols1:
    print(eachCol1.text)

time.sleep(5)
print("------------------------------")

multipleCols2=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[6]/td")

for eachCol2 in multipleCols2:
    print(eachCol2.text)

time.sleep(2)
driver.close()