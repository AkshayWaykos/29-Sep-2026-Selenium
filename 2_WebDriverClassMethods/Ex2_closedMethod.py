import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com/")

time.sleep(2)

driver.close()           #to close the single tab of browser.


