import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(2)
doubleClick=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")

act=ActionChains(driver)
time.sleep(2)

#Approach 1
# act.move_to_element(doubleClick).perform()
# act.double_click().perform()

#Approach 2
# act.move_to_element(doubleClick).double_click().perform()

#Approach 3
act.double_click(doubleClick).perform()


#pop-up handled
time.sleep(4)
pop=driver.switch_to.alert
pop.accept()

time.sleep(5)
driver.close()
