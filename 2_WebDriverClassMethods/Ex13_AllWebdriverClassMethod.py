import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.google.com/")

driver.fullscreen_window()
time.sleep(2)

driver.minimize_window()
time.sleep(2)

driver.maximize_window()
time.sleep(2)

print(driver.title)
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.execute_script("window.open('https://www.facebook.com')")
time.sleep(2)
print(driver.current_url)


driver.close()      #---> use for single table closed

driver.quit()      #-->Use to close all tab.