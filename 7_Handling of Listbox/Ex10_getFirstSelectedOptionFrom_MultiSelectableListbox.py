import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

color=driver.find_element(By.XPATH,"//select[@id='colors']")

c=Select(color)

c.select_by_value("red")
c.select_by_index(2)
c.deselect_by_visible_text("Green")

time.sleep(2)
#Apr 1
c1=c.first_selected_option
firstOptionValu=c1.text
print(firstOptionValu)

#Apr 2
c2=c.first_selected_option.text
print(c2)

#Apr 3:
print(c.first_selected_option.text)

time.sleep(2)
driver.close()