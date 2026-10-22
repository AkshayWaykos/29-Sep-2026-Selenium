import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
#Page will open
driver.get("https://www.flipkart.com/")

time.sleep(4)
#Mobile no will enter on colorfull pop-up
driver.find_element(By.XPATH,"//input[@type='number']").send_keys("9911882277")

time.sleep(4)
#Click on X (cross button)
driver.find_element(By.XPATH,"//span[@class='b3wTlE']").click()

driver.close()
