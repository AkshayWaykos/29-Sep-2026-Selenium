import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(2)

#click on NewTab from main page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()
time.sleep(4)

#get child window ID
allIds=driver.window_handles      #[mainPageId[0], childWindowId[1]]

#Switch to Child Window1
driver.switch_to.window(allIds[1])      #String ChildWindowId

time.sleep(10)
#click on Training Link from Child Window
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()
time.sleep(2)

#Switch to main page
driver.switch_to.window(allIds[0])
time.sleep(2)

#click on NewWindow from mainPage
driver.find_element(By.XPATH,"//input[@name='NewWindow']").click()

#get all Ids
AllIds2=driver.window_handles       #[mainPageId[0], childWindowId1[1], childWindowId2[2]]

#Switch to Child Window2
driver.switch_to.window(AllIds2[2])
time.sleep(2)
driver.close()




time.sleep(10)
