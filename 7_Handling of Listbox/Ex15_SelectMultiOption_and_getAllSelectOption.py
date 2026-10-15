import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
allAnimals=driver.find_element(By.XPATH,"//select[@id='animals']")
time.sleep(2)

aa=Select(allAnimals)

aa.select_by_index(0)
aa.select_by_value("cheetah")
aa.select_by_visible_text("Deer")

allselectAnimalCount=aa.all_selected_options

for eachselectedoption in allselectAnimalCount:
    ASAnimal=eachselectedoption.text
    print(ASAnimal)

print("---------------------------")
allA=aa.options

for eachAnimal in allA:
    AllAni=eachAnimal.text
    print(AllAni)


time.sleep(2)
driver.close()