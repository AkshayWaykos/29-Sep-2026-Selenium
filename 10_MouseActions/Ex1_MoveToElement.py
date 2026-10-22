import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.amazon.in/")

time.sleep(8)
signIn=driver.find_element(By.XPATH,"//span[text()='Hello, sign in']")

act=ActionChains(driver)

act.move_to_element(signIn).perform()

time.sleep(8)
driver.find_element(By.XPATH,"//span[text()='Your Wish List']").click()

time.sleep(8)
driver.close()

