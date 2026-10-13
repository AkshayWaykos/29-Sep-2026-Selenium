import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

attributeval1=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute('placeholder')
print(attributeval1)
time.sleep(2)

attributeval2=driver.find_element(By.XPATH,"//input[@id='email']").get_attribute('placeholder')
print(attributeval2)

print("---------------------------------------------------------------------------------")
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Akshay")
time.sleep(2)

ValueAttrInfo=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("value")
print("Value for name filed=",ValueAttrInfo)


driver.close()