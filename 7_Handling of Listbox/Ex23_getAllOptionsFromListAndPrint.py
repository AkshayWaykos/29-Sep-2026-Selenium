import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

countryList=driver.find_element(By.XPATH,"//select[@id='country']")

s=Select(countryList)

show=s.options
print(len(show))

for eachCountry in show:
    print(eachCountry.text)

time.sleep(1)
driver.close()