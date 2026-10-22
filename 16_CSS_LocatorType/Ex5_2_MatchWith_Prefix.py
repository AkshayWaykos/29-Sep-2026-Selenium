import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)


driver.find_element(By.CSS_SELECTOR,"[placeholder^='Name']").send_keys("Kiyansh")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"[class^='st']").click()         # 1st Approach

time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"button[class^='st']").click()   #2nd Approach

time.sleep(4)
driver.close()