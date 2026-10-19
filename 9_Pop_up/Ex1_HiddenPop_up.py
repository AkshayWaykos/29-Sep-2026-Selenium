import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://www.mobikwik.com/")

time.sleep(2)
#click on Login option on mobikwik page
driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()

time.sleep(4)
#enter mobile no.
driver.find_element(By.XPATH,"//input[@inputmode='numeric']").send_keys("9988776655")

time.sleep(5)
driver.close()