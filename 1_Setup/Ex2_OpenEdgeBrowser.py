import time

from selenium import webdriver

driver=webdriver.Edge()
driver.get("https://www.facebook.com")

print(driver.title)
print("Edge Browser Open Successfully")

time.sleep(4)

driver.quit()