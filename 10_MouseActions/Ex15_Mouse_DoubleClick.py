import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(4)
screenDown=driver.find_element(By.XPATH,"//h2[contains(text(),'Drag and Drop')]")
act=ActionChains(driver)
act.scroll_to_element(screenDown).perform()

time.sleep(5)
doubleClick=driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")

act.move_to_element(doubleClick).perform()
act.double_click().perform()

time.sleep(5)
driver.close()
