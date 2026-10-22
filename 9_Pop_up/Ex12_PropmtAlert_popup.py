import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,600)")

buttonTxt=driver.find_element(By.XPATH,"//button[text()='Prompt Alert']")
print(buttonTxt.text)

time.sleep(2)
buttonTxt.click()

time.sleep(2)
popup=driver.switch_to.alert
print(popup.text)

time.sleep(2)
popup.send_keys("Kiyansh")

time.sleep(2)
popup.accept()

time.sleep(2)
msg=driver.find_element(By.XPATH,"//p[@id='demo']")
print(msg.text)

time.sleep(2)
driver.close()