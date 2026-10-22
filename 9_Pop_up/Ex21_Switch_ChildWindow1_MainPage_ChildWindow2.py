import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://skpatro.github.io/demo/links/")

time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()

time.sleep(5)
windowIds=driver.window_handles
driver.switch_to.window(windowIds[1])

time.sleep(5)
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()

time.sleep(5)
driver.switch_to.window(windowIds[0])

time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='NewWindow']").click()

time.sleep(5)
windowId2=driver.window_handles
driver.switch_to.window(windowId2[2])

time.sleep(5)
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH,"(//span[text()='WebdriverIO'])[1]").click()

time.sleep(5)
driver.switch_to.window(windowId2[0])

time.sleep(5)
driver.quit()
