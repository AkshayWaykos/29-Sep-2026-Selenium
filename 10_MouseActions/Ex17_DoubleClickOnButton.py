import time
from os import name

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,1000)")

time.sleep(5)
buttonDouble=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")
act=ActionChains(driver)

act.double_click(buttonDouble).perform()

afterClick=driver.find_element(By.XPATH,"//p[contains(text(),'Double click on button, the text from Field1 will be copied into Field2.')]")
print(afterClick.text)


time.sleep(5)
driver.close()