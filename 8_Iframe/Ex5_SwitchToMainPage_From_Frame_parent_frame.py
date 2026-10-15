import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

time.sleep(2)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))

driver.find_element(By.XPATH,"//button[@type='button']").click()

driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()


time.sleep(2)
driver.close()

