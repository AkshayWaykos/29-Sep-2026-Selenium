import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

time.sleep(5)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))

time.sleep(2)
driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time.')]")

time.sleep(2)
driver.switch_to.default_content()

driver.find_element(By.XPATH,"//a[@id='tryhome']")
time.sleep(2)
driver.close()

