import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.execute_script("window.scroll(0,1200)")

time.sleep(2)
Options=driver.find_element(By.XPATH,"//select[@id='colors']")
print(Options.text)

s=Select(Options)

s.select_by_value("blue")
s.select_by_index(4)
s.select_by_visible_text("Yellow")

print("--------------------")
time.sleep(5)
firstOption=s.first_selected_option.text
print("First Selected Options=",firstOption)
print("--------------------")

time.sleep(5)
s.deselect_by_value("blue")
s.deselect_by_index(4)
s.deselect_by_visible_text("Yellow")
print("Deselected Done")
print("--------------------")
print(s.is_multiple)


time.sleep(4)
driver.close()