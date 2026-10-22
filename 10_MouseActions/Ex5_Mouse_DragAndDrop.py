import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.guru99.com/test/drag_drop.html")
time.sleep(2)
driver.execute_script("window.scroll(0,300)")

time.sleep(5)
source=driver.find_element(By.XPATH,"(//a[@class='button button-orange'])[2]")
destination=driver.find_element(By.XPATH,"(//li[@class='placeholder'])[2]")

act=ActionChains(driver)

#Approach 1    (just click on source and move destination but not drop there)
# act.drag_and_drop(source,destination).perform()


time.sleep(5)
#Approach 2
act.move_to_element(source).click_and_hold().move_to_element(destination).release().perform()


time.sleep(5)
driver.close()


