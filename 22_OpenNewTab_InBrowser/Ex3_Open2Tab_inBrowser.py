import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(2)

driver.execute_script("window.open(' ')")

driver.switch_to.window(driver.window_handles[1])
driver.get("https://web.whatsapp.com/")
print(driver.title)
time.sleep(2)

driver.execute_script("window.open(' ')")

driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.youtube.com/")
print(driver.title)
time.sleep(2)

driver.execute_script("window.open(' ')")

driver.switch_to.window(driver.window_handles[0])
print(driver.title)
time.sleep(5)

driver.quit()

