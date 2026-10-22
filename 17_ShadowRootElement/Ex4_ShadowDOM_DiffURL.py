
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://selectorshub.com/xpath-practice-page/")


driver.execute_script("window.scroll(0,1900)")
time.sleep(4)

userName=driver.find_element(By.XPATH,"//div[@id='userName']").shadow_root.find_element(By.CSS_SELECTOR,"#kils")
userName.send_keys("Akshay")

time.sleep(5)
driver.close()
