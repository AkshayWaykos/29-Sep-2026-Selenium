import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,100)")


dynamicButton=driver.find_element(By.XPATH,"//button[@class='start' or @class='stop']")
# dynamicButton=driver.find_element(By.XPATH,"//button[@name='start' or @name='stop']")
# dynamicButton=driver.find_element(By.XPATH,"//button[text()='STOP' or text()='STOP']")
# dynamicButton=driver.find_element(By.XPATH,"//button[starts-with(@name,'st')]")
# dynamicButton=driver.find_element(By.XPATH,"//button[starts-with(text(),'ST')]")


print(dynamicButton.text)

time.sleep(10)
#click on Start
dynamicButton.click()

time.sleep(10)

#click on STOP
dynamicButton.click()

time.sleep(10)
#click on Start
dynamicButton.click()



time.sleep(8)
driver.close()