import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

#Switch to outer frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))

#get text of outer frame
Outeriframe=driver.find_element(By.XPATH,"//p[text()='Outer iframe']").text
print(Outeriframe)

#Switch to inter/nester frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

#get text of inter/nester frame
Inneriframe=driver.find_element(By.XPATH,"//p[text()='Inner iframe content']").text
print(Inneriframe)

time.sleep(2)
driver.close()


