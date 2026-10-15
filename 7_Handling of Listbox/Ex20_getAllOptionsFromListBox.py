import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

allAnimals=driver.find_element(By.XPATH,"//select[@id='animals']")

am=Select(allAnimals)

allAni=am.options

for eachAnimal in allAni:
    print(eachAnimal.text)

print("======================")

allAniCount=am.options
size=len(allAniCount)
print(size)

time.sleep(2)
driver.close()