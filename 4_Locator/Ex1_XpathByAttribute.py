import time

print("======Xpath By Attribute======")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name'] ").send_keys("Akshay Waykos")
print("Enter Name=",driver.title)
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Akki@gmail.com")
print("Mail Id Enter=",driver.title)
time.sleep(2)
driver.execute_script("window.scrollTo(0,500);")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='male']").click()
print("click on Gender Details= ",driver.title)
time.sleep(2)
driver.execute_script("window.scrollTo(0,1000);")
time.sleep(4)
driver.execute_script("window.scrollTo(0,800);")
time.sleep(4)
driver.find_element(By.XPATH,"//a[text()='Apple']").click()
print(" Select Apple Text =",driver.title)
time.sleep(2)
driver.close()