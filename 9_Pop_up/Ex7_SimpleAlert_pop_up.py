import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.execute_script("window.scroll(0,500)")
time.sleep(2)

button=driver.find_element(By.XPATH,"//button[text()='Simple Alert']")
print(button.text)

time.sleep(2)
button.click()

time.sleep(2)
alt=driver.switch_to.alert
print(alt.text)

time.sleep(2)
alt.accept()

time.sleep(2)
driver.close()