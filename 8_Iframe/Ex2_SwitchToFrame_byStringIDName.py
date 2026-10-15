import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

time.sleep(2)

#Switch to frame  ---> #String id/name of the frame   (Approch 2)
driver.switch_to.frame("iframeResult")


driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time.')]").click()

driver.close()