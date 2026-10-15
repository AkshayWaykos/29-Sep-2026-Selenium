import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

allOptions=driver.find_element(By.XPATH,"//select[@id='colors']")

op=Select(allOptions)

op.select_by_index(1)
op.select_by_index(2)
op.select_by_index(3)

result=op.all_selected_options

for eachSelected in result:
    print("Total selected Option from list box =",eachSelected.text)

print("=======================================")

selectOfAllSelectedOption=op.all_selected_options
size=len(selectOfAllSelectedOption)
print("Total Selected option from list box =",size)

time.sleep(2)
driver.close()