import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

driver=webdriver.Firefox()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(2)

#click on NewTab from main page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()

#get child window ID
time.sleep(2)
allIds=driver.window_handles
childWindow=allIds[1]

#Switch to Child Window
time.sleep(2)
driver.switch_to.window(childWindow)

#click on Training Link from Child Window
time.sleep(2)
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()

time.sleep(5)
driver.close()