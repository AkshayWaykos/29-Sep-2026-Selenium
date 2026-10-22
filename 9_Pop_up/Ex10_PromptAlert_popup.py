import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)
driver.execute_script("window.scroll(0,500)")

time.sleep(2)
buttonText=driver.find_element(By.XPATH,"//button[text()='Prompt Alert']")
print(buttonText.text)
buttonText.click()

popUp=driver.switch_to.alert
print(popUp.text)

time.sleep(2)
popUp.send_keys("Trupti")

time.sleep(2)
popUp.accept()

time.sleep(2)
msg=driver.find_element(By.XPATH,"//p[@id='demo']")
print(msg.text)

time.sleep(2)
driver.close()
