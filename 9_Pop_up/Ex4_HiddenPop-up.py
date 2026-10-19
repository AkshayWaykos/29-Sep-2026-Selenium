import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://www.mobikwik.com/")

time.sleep(2)
driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()

time.sleep(2)
driver.find_element(By.XPATH,"//input[@inputmode='numeric']").send_keys("9911882233")

time.sleep(2)
driver.close()
