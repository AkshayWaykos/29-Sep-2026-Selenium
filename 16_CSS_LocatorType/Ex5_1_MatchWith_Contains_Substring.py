import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[placeholder*='Name']").send_keys("Akshay")

driver.find_element(By.CSS_SELECTOR,"input[placeholder*='Mail']").send_keys("abc@gmail.com")

driver.find_element(By.CSS_SELECTOR,"button[class*='st']").click()

driver.find_element(By.CSS_SELECTOR,"input[value*='female']").click()

time.sleep(4)
driver.close()


