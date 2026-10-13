
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")

#contain test
driver.find_element(By.XPATH,"//a[contains(text(),'Download')]").click()

time.sleep(2)
