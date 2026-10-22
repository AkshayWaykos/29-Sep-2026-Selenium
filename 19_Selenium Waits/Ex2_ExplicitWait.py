import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")


##Wait to for element to visible
wait=WebDriverWait(driver,5)
element=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[text()='STAT']")))
element.click()

time.sleep(5)

#Wait for element to be clickable
wait = WebDriverWait(driver, 3)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Simple Alert']")) )
element.click()

#check alert present or not.
#Wait for element to be clickable
wait = WebDriverWait(driver, 5)
element = wait.until(EC.alert_is_present() )

time.sleep(4)
driver.quit()

