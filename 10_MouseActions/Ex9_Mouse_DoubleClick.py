import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/#")

time.sleep(5)
driver.execute_script("window.scroll(0,1000)")

time.sleep(5)
doubleClick=driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")

act=ActionChains(driver)

time.sleep(5)
act.move_to_element(doubleClick).perform()
act.double_click().perform()

time.sleep(10)
driver.close()