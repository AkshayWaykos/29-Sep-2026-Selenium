from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

text1=driver.find_element(By.XPATH,"//p[contains(text(),'CPU load of Chrome process: ')]").text
print(text1)

text2=driver.find_element(By.XPATH,"//h2[contains(text(),'Dynamic Web Table')]").text
print(text2)

text3=driver.find_element(By.XPATH,"//a[contains(text(),'Data Entry Form')]").text
print(text3)

driver.close()
