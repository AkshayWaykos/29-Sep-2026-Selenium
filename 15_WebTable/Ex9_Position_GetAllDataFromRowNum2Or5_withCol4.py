import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(4)

time.sleep(4)
position1and5FromCol4=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[position()=2 or position()=6 ]/td[4]").text

print(position1and5FromCol4)

time.sleep(4)
driver.close()