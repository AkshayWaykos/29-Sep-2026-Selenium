import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

color=driver.find_element(By.XPATH,"//select[@id='colors']")

c=Select(color)

c.select_by_index(0)
c.select_by_value("blue")
c.select_by_visible_text("Yellow")

time.sleep(5)

c.deselect_by_index(0)
time.sleep(2)
c.deselect_by_value("blue")
time.sleep(2)
c.deselect_by_visible_text("Yellow")
time.sleep(2)



driver.close()
