import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

multiS=driver.find_element(By.XPATH,"//select[@id='colors']")

m=Select(multiS)

result=m.is_multiple
print(result)

if result:
    print("Listbox is of Multi Selectable type")
else:
    print("Listbox is of Single Selectable type")

time.sleep(2)
driver.close()

