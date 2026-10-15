import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

singleSelected=driver.find_element(By.XPATH,"//select[@id='country']")

SS=Select(singleSelected)

result1=SS.is_multiple
print(result1)

if result1:
    print("Listbox is Multi Selected drop-down")
else:
    print("Listbox is Single selected drop-down")

time.sleep(4)


print("---------------------------------------------------------------------")
multiSelected=driver.find_element(By.XPATH,"//select[@id='colors']")

MS=Select(multiSelected)

result2=MS.is_multiple
print(result2)

if result2:
    print("Listbox is Multi Selected drop-down")
else:
    print("Listbox is Single selected drop-down")


time.sleep(2)
driver.close()