import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sagar")

time.sleep(2)
attributevalue1=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("value")
print("Name filed attribute value =",attributevalue1)
print("----------------------------------")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abcd@gmail.com")
time.sleep(2)

attributevalue2=driver.find_element(By.XPATH,"//input[@id='email']").get_attribute("value")
print("Email filed attribute value =",attributevalue2)
