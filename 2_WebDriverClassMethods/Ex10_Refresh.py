import time
from fileinput import close

print("========Refresh Method===========")

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com/")
time.sleep(2)
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.back()           #Backword Page
time.sleep(2)
driver.refresh()        #Refresh Page
time.sleep(2)
driver.forward()        #Forward page
time.sleep(2)
driver.close()          #closed browser
