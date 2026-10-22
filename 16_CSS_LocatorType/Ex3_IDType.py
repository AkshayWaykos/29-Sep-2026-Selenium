import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.CSS_SELECTOR,"#male").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input#sunday").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"*#phone").send_keys("9922338844")
time.sleep(2)


driver.close()

