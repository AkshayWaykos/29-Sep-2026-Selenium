import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/#")

driver.execute_script("window.scroll(0,1500)")

time.sleep(5)

source=driver.find_element(By.XPATH,"//div[@id='draggable']")
destination=driver.find_element(By.XPATH,"//div[@id='droppable']")

act=ActionChains(driver)

act.drag_and_drop(source,destination).perform()


time.sleep(5)
driver.close()