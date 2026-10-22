import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='New Tab']").click()

time.sleep(5)
allIds=driver.window_handles

time.sleep(5)
driver.switch_to.window(allIds[1])

time.sleep(5)
newWindowTitle=driver.find_element(By.XPATH,"//h1[@class='title']").text
print(newWindowTitle)

time.sleep(5)
driver.switch_to.window(allIds[0])

time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Popup Windows']").click()

time.sleep(5)
driver.maximize_window()

time.sleep(5)
driver.close()







