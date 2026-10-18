import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

time.sleep(2)
#step 1 - handle outer frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))
#print outer print text details
outFrame=driver.find_element(By.XPATH,"//p[contains(text(),'Outer iframe')]")
print("Outer Frame Text = ",outFrame.text)

time.sleep(2)
#step 2 - handle Inner frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))
#print Inner print text details
innerFrame=driver.find_element(By.XPATH,"//p[contains(text(),'Inner iframe content')]")
print("Inner Frame Text = ",innerFrame.text)

time.sleep(2)
driver.close()