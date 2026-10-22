import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,1000)")
time.sleep(5)

filed1=driver.find_element(By.XPATH,"//input[@id='field1']")

act=ActionChains(driver)

act.move_to_element(filed1).perform()
act.context_click().perform()


time.sleep(5)
driver.close()
