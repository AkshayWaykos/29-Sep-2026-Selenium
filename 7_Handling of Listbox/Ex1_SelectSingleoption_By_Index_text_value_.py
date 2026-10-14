
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

#step 1 - Find the list box path
country=driver.find_element(By.XPATH,"//select[@id='country']")            #country = web element object

#step 2 -create object of Select class which accepts the listbox element as argument
s=Select(country)

#Step 3: call Select methods (selectByIndex, selectByValue, selectByVisibleText)

s.select_by_index(5)                  #int index
s.select_by_visible_text("India")     #String text
s.select_by_value("china")            #string value

time.sleep(5)