import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()

driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//button[@class='start']").click()

driver.close()
