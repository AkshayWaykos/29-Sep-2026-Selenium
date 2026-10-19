from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

allOptions=driver.find_element(By.XPATH,"//select[@id='country']")

ap=Select(allOptions)

showAllOptions=ap.options

for eachOptions in showAllOptions:
    print(eachOptions.text)
print("-------------------------")

showallSize=ap.options
print(len(showallSize))

print("-------------------------")

