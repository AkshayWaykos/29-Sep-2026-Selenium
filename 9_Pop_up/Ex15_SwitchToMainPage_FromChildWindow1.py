import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

driver=webdriver.Firefox()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(2)


driver.find_element(By.XPATH,"//input[@name='NewTab']").click()

time.sleep(2)
allIds=driver.window_handles
childWindowsId=allIds[1]

time.sleep(2)
driver.switch_to.window(childWindowsId)


time.sleep(4)
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()

time.sleep(2)
driver.switch_to.window(allIds[0])

time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='NewWindow']").click()

time.sleep(2)
driver.maximize_window()

time.sleep(2)
driver.quit()