import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

lengthOfAllRow=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(lengthOfAllRow))


time.sleep(2)
driver.close()