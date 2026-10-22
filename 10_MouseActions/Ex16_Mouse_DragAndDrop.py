import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,1700)")


time.sleep(5)
#Drag and Drop
boxOne=driver.find_element(By.XPATH,"//div[@id='draggable']")
boxTwo=driver.find_element(By.XPATH,"//div[@id='droppable']")

act=ActionChains(driver)

act.drag_and_drop(boxOne,boxTwo).perform()
time.sleep(10)

#Slider Handle
source=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
destination=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")


time.sleep(2)
act.move_to_element(source).click_and_hold().move_to_element(destination).release().perform()

time.sleep(5)
driver.close()