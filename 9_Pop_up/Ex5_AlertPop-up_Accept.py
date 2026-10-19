import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.guru99.com/test/delete_customer.php")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("4567")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='submit']").click()

popup=driver.switch_to.alert
print(popup.text)

time.sleep(2)
popup.accept()

time.sleep(2)
print(popup.text)

time.sleep(2)
popup.accept()

time.sleep(2)
driver.close()

