import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
#step 1 - find list xpath
text=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")

#step 2 = create select class object

tt=Select(text)

#step 3 =call select class method

tt.select_by_visible_text("Option2")         #check through Text
print("Option 2 selected from List dropdown through text method.")
time.sleep(2)
driver.close()