import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

time.sleep(2)
#switch to Outer Frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))

time.sleep(2)
#print outer frame text.
outerText=driver.find_element(By.XPATH, "//p[contains(text(),'Outer iframe')]")
print(outerText.text)

#Switch to Inner Frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

time.sleep(2)
#print Inner frame text.
innerText=driver.find_element(By.XPATH,"//p[contains(text(),'Inner iframe content')]")
print(innerText.text)


time.sleep(2)
driver.close()




