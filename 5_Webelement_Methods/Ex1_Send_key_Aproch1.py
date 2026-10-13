import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Kiyansh")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Kia@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys('9988776655')
time.sleep(2)
print(driver.title)
driver.close()