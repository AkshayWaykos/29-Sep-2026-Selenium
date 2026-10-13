import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

name=driver.find_element(By.XPATH,"//input[@id='name']")
name.send_keys("Kiyansh")

email=driver.find_element(By.XPATH,"//input[@id='email']")
email.send_keys("abc@gmail.com")

phone=driver.find_element(By.XPATH,"//input[@id='phone']")
phone.send_keys("9977553311")

time.sleep(2)

print(driver.title)
driver.close()