import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com")
print(driver.title)
print("FireBox Browser Open Successfully")

time.sleep(5)

driver.quit()