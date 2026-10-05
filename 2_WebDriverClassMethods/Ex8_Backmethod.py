import time

print("===Back Method===")

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com/")
time.sleep(2)
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.back()   #TO do the backward
time.sleep(2)
driver.close()