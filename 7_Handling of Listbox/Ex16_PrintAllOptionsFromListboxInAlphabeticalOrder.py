import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

print("===Assignment4_PrintAllOptionsFromListboxInAlphabeticalOrder==")

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

AllOption=driver.find_element(By.XPATH,"//select[@id='colors']")
AO=Select(AllOption)

AOP=AO.options

all_options_list =[]   #first create empty list it will use to store list

for eachOption in AOP:
    all_options_list.append(eachOption.text)

#with the help of sorted order
for show in sorted(all_options_list):
    print(show)

time.sleep(2)
driver.close()


#OutPut -->

# Blue
# Green
# Green
# Red
# Red
# White
# Yellow
