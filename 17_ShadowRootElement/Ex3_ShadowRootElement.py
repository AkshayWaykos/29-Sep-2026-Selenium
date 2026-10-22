import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(4)
driver.execute_script("window.scroll(0,3000)")

driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Sagar")

time.sleep(4)
driver.close()

