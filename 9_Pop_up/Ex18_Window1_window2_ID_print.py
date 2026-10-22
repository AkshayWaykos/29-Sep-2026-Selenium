import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(5)

#click on New Tab button to switch on new window
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()
time.sleep(5)
windowIds=driver.window_handles
mainWindowId=windowIds[0]
childWindowId=windowIds[1]


print(mainWindowId)
print(childWindowId)


time.sleep(5)
driver.close()