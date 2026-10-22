import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://facebook.com/")
time.sleep(2)

currentURL=driver.current_url

print(currentURL)

print("============================")

print(driver.current_url)


time.sleep(5)
driver.close()
