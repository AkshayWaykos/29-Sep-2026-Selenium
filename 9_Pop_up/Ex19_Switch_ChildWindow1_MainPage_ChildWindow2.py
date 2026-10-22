import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(5)

#Click on NewTab Button to move on New Windows
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()

#to handle new screen use below code
allIds=driver.window_handles

driver.switch_to.window(allIds[1])

time.sleep(10)
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()

time.sleep(10)
driver.switch_to.window(allIds[0])

time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='NewWindow']").click()

time.sleep(10)
allIds2=driver.window_handles

driver.switch_to.window(allIds2[2])

time.sleep(5)
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH,"(//span[text()='HOME'])[1]").click()

time.sleep(5)
driver.switch_to.window(allIds2[0])


time.sleep(5)
driver.close()





