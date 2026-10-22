import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()

time.sleep(4)
driver.get("https://testautomationpractice.blogspot.com/")

footerLinks=driver.find_element(By.XPATH,"//h2[contains(text(),'Footer Links')]")
act=ActionChains(driver)

act.scroll_to_element(footerLinks).perform()

time.sleep(4)
doubleClickButton=driver.find_element(By.XPATH,"//h2[contains(text(),'Double Click')]")

act.scroll_to_element(doubleClickButton).perform()


time.sleep(20)
driver.close()