import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

#switch to Outer ifram
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))

#get text of out iframe
outerFrame=driver.find_element(By.XPATH,"//p[text()='Outer iframe']").text
print(outerFrame)

time.sleep(2)
#switch to Inter/Nester iframe
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

#get text of Inter/Nester iframe
InnerFrame=driver.find_element(By.XPATH,"//p[text()='Inner iframe content']").text
print(InnerFrame)

#driver.switch_to.parent_frame()
driver.switch_to.default_content()


#get text of Home element from main page
home=driver.find_element(By.XPATH,"//a[text()='Home'][1]").text
print(home)

driver.close()

