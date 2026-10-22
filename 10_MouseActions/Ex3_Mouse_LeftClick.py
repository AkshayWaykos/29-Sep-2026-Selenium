import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.amazon.in/")

time.sleep(10)
allMenu=driver.find_element(By.XPATH,"//a[@id='nav-hamburger-menu']")

act=ActionChains(driver)

#Approach 1
# act.move_to_element(allMenu).perform()
# act.click().perform()

#Approach 2
# act.move_to_element(allMenu).click().perform()

#Approach 3

act.click(allMenu).perform()


time.sleep(5)
#menus closed with X button
driver.find_element(By.XPATH,"//div[@aria-label='Close menu']").click()

time.sleep(2)
driver.close()