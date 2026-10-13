import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

text1=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[2]").text
print("Through Absolute Xpath print text= ",text1)


text2=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[3]/td[2]").text
print("Through Absolute Xpath print text= ",text2)

text3=driver.find_element(By.XPATH,"//table[@id='productTable']/tbody/tr[1]/td[3]").text
print("Through Absolute Xpath print text= ",text3)

text4=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr[4]/td[1]").text
print("Through Absolute Xpath print text= ",text4)

time.sleep(2)