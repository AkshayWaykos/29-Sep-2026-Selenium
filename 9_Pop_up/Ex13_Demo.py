import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)
driver.execute_script("window.scroll(0,600)")

time.sleep(2)
button=driver.find_element(By.XPATH,"//button[text()='Prompt Alert']")
print(button.text)
button.click()

time.sleep(2)
alt=driver.switch_to.alert
print(alt.text)

time.sleep(2)
alt.send_keys("Sagar Bro..")

time.sleep(2)
alt.accept()

time.sleep(2)
msg=driver.find_element(By.XPATH,"//p[@id='demo']")
print(msg.text)

time.sleep(2)
driver.close()