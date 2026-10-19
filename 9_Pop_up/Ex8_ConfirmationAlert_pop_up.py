import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.execute_script("window.scroll(0,500)")
time.sleep(2)

button=driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']")
print(button.text)
button.click()


time.sleep(2)
confirmationPop_up=driver.switch_to.alert
print(confirmationPop_up.text)

time.sleep(2)
confirmationPop_up.accept()

time.sleep(2)
driver.close()

