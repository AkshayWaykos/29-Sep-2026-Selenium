import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.amazon.in/")

time.sleep(10)
Electronics=driver.find_element(By.XPATH,"//a[text()=' Electronics ']")

act=ActionChains(driver)

#Approach 1
# act.move_to_element(Electronics).perform()
# act.context_click().perform()

#Approach 2
# act.move_to_element(Electronics).context_click().perform()

#Approach 3
act.context_click(Electronics).perform()

time.sleep(5)
driver.close()