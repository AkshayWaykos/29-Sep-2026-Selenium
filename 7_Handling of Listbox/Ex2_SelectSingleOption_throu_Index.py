import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(3)
#step 1 = find element from list
listB=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")

#step 2 = create select class object
lb=Select(listB)

#step 3 = select option from dropdown list through select by index

lb.select_by_index(2)
print("Option 2 selected from List dropdown through index method.")
time.sleep(2)
driver.close()
