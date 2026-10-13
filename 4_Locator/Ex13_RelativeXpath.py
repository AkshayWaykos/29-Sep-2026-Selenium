
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

text1=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[3]").text
print("Through Relative Xpath print text= ",text1)

text2=driver.find_element(By.XPATH,"//table[@id='taskTable']//tr[2]/td[3]").text
print("Through Relative Xpath print text= ",text2)

text3=driver.find_element(By.XPATH,"//table[@id='taskTable']//tr[2]/td[1]").text
print("Through Relative Xpath print text= ",text3)

driver.close()
