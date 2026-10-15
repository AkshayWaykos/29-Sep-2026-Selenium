import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v151.fed_cm import select_account
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

multiC=driver.find_element(By.XPATH,"//select[@id='colors']")

mc=Select(multiC)

mc.select_by_index(0)
mc.select_by_value("blue")
mc.select_by_visible_text("Green")

time.sleep(4)

mc.deselect_by_index(0)
mc.deselect_by_value("blue")
mc.deselect_by_visible_text("Green")

time.sleep(2)
driver.close()