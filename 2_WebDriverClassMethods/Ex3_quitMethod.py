print("==WebDriver Method --> Quit Method==")

import time
from selenium import webdriver

driver=webdriver.Firefox()
driver.get('https://www.google.com/')
time.sleep(5)
driver.execute_script("window.open('https://www.youtube.com')")
time.sleep(5)
driver.execute_script("window.open('https://www.facebook.com')")

time.sleep(5)

driver.quit()      #closed all time from browser
