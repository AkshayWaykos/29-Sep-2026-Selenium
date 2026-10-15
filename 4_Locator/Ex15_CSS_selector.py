import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'#name').send_keys("Akshay")

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'.form-control').send_keys("abcd@gmail.com")

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'#phone').send_keys("9988665544")

driver.close()

# = ID ke liye      -> #name
# . = Class ke liye -> .email
# tag = Tag ke liye -> input