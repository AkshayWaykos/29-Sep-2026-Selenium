import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")

#contain = Attributes
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Name')]").send_keys("ABCD")

driver.find_element(By.XPATH,"//input[contains(@placeholder,'EMail')]").send_keys("xyz@gmail.com")

time.sleep(5)