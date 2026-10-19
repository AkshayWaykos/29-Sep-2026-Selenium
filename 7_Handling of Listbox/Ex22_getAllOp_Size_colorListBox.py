from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

allColors=driver.find_element(By.XPATH,"//select[@id='colors']")
ac=Select(allColors)
allOptions=ac.options

for eachOptions in allOptions:
    print(eachOptions.text)

print("---------------------------")

allOptionsCount=ac.options
print(len(allOptionsCount))

print("---------------------------")