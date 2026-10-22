import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys("Kiyansh")
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,".form-control").send_keys("Akshay")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"*.form-control").send_keys("Sagar")
# time.sleep(2)

time.sleep(4)
driver.close()