import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

#Step 1 = find xpath of list and save in one object
val=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")

#Step 2 create select class object

v=Select(val)

#Step 3 call the method of select class
v.select_by_value("option3")
print("Option 3 selected from List dropdown through value method.")
time.sleep(2)

driver.close()

