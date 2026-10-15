import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

allOptios =driver.find_element(By.XPATH,"//select[@id='colors']")

ap=Select(allOptios)

showAllOptions=ap.options

for eachOption in showAllOptions:
    print(eachOption.text)

time.sleep(2)
driver.close()
