import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.guru99.com/test/drag_drop.html")
driver.execute_script("window,scroll(0,400)")

time.sleep(2)
sour_5000=driver.find_element(By.XPATH,"(//a[@class='button button-orange'])[2]")
desc_AmtDr=driver.find_element(By.XPATH,"(//li[@class='placeholder'])[2]")

action=ActionChains(driver)

#Approach 1
action.drag_and_drop(sour_5000,desc_AmtDr).perform()

time.sleep(5)

sour_bankOpt=driver.find_element(By.XPATH,"(//a[@class='button button-orange'])[5]")
desc_accountOpt=driver.find_element(By.XPATH,"(//li[@class='placeholder'])[1]")


#Approach 2
action.move_to_element(sour_bankOpt).click_and_hold().move_to_element(desc_accountOpt).release().perform()


time.sleep(10)
driver.close()
