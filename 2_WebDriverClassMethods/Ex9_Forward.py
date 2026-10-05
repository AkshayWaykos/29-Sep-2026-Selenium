import time

print("============Forward page==================")

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(2)
driver.get("https://www.facebook.com/")
print(driver.title)
time.sleep(2)
driver.back()        #backword page
print(driver.title)
time.sleep(2)
driver.forward()     #Forward page
print(driver.title)
time.sleep(2)

driver.close()