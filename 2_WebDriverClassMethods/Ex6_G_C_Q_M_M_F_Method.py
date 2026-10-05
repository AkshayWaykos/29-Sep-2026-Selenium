import time
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("https://www.google.com/")
print(driver.title)
time.sleep(10)

driver.execute_script("window.open('https://www.youtube.com')")
time.sleep(10)
print(driver.title)

driver.execute_script("window.open('https://www.facebook.com')")
time.sleep(10)
print(driver.title)


driver.quit()