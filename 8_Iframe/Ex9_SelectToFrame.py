
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
time.sleep(4)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
print("Enter the Outer frame")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='button']").click()
print("Click on button")
time.sleep(2)

driver.switch_to.default_content()
print("Exit from frame")
time.sleep(2)
driver.find_element(By.XPATH,"//a[@id='tryhome']").click()
print("Click on Home Button which is present outside of frame")
time.sleep(2)

driver.close()



