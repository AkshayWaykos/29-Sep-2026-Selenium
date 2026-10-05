import time
from unittest import expectedFailure

print("=====Title Method=====")

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com/")
time.sleep(2)
driver.get("https://www.facebook.com/")
time.sleep(2)

print(driver.title)       # Title print 1st way

print("-----------")

actuaTitle=driver.title
expTitle="Facebook"

if actuaTitle==expTitle:
    print("Proper Page loaded")

time.sleep(2)
