import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(4)

getValueFromColom=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[position()=2 or position()=4]/td[4]").text

print(getValueFromColom)

time.sleep(4)
driver.close()