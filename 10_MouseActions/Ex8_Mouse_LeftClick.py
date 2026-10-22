import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")

time.sleep(5)
hamburgerButton=driver.find_element(By.XPATH,"(//yt-icon-button[@id='guide-button'])[1]")

act=ActionChains(driver)

#Approach 1
# act.move_to_element(hamburgerButton).click().perform()

#Approach 2
# act.move_to_element(hamburgerButton).perform()
# act.click().perform()

#Approach 3
act.click(hamburgerButton).perform()

time.sleep(5)
driver.find_element(By.XPATH,"//yt-formatted-string[contains(text(),'Shorts')]").click()

time.sleep(30)
driver.close()

