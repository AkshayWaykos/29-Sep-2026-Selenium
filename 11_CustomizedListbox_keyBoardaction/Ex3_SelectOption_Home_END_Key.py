import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,900)")
time.sleep(2)

country=driver.find_element(By.XPATH,"//select[@id='country']")

country.click()
time.sleep(5)

country.send_keys(Keys.END)
time.sleep(5)
country.send_keys(Keys.HOME)

time.sleep(5)
driver.close()