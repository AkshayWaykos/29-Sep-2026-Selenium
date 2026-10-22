import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

detailsName = driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='text']")
detailsName.send_keys("Sagar")
print(detailsName.text)

time.sleep(4)

driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()

time.sleep(3)

word=driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,".info")
print(word.text)

time.sleep(3)
driver.close()
