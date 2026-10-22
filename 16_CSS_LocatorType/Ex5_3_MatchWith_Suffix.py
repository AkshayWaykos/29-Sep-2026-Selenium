import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)


driver.find_element(By.CSS_SELECTOR,"input[placeholder$='Name']").send_keys("Kiyansh")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[placeholder$='EMail']").send_keys("xyz")

time.sleep(4)
driver.close()