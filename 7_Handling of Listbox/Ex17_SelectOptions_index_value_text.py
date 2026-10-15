import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#step 1 = find list box xpath
options=driver.find_element(By.XPATH,"//select[@id='country']")

#Step 2 = Create select class object to call methods
selectOpt=Select(options)

#step 3 = call methods of select class

selectOpt.select_by_index(2)                #Select By Index
time.sleep(4)
selectOpt.select_by_value("canada")         #select by Value
time.sleep(4)
selectOpt.select_by_visible_text("Japan")   #Select By Visible text

time.sleep(2)
driver.close()