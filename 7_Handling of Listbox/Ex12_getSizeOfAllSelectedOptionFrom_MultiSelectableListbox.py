import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

AllColor=driver.find_element(By.XPATH,"//select[@id='colors']")

ac=Select(AllColor)

ac.select_by_index(3)
ac.select_by_index(2)
ac.select_by_index(1)
ac.select_by_index(0)

#Apr 1
sizeofAllSelectedOptions=ac.all_selected_options
size1 = len(sizeofAllSelectedOptions)
print(size1)

#Apr 2
size=len(ac.all_selected_options)
print(size)

#Apr3
print(len(ac.all_selected_options))



time.sleep(2)
driver.close()