import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#Fluent Wait
wait = WebDriverWait(driver,
           timeout=5,             # timeInSec
           poll_frequency=1,       # check after every 1 second
           ignored_exceptions=[NoSuchElementException])


element = wait.until( EC.visibility_of_element_located((By.XPATH, "//button[text()='START']")) )
element.click()


#Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Simple Alert']")) )
element.click()


#check alert present or not
#Wait for element to be clickable
element = wait.until(EC.alert_is_present() )

time.sleep(10)