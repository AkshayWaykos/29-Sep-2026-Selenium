import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.execute_script("window.scroll(0,200)")

driver.find_element(By.CSS_SELECTOR,"input[class='form-control']:nth-of-type(1)").send_keys("Akshay")


driver.find_element(By.CSS_SELECTOR,"input[class='form-control']:nth-of-type(2)").send_keys("Abc@gmail.com")

driver.find_element(By.CSS_SELECTOR,"input[class='form-control']:nth-of-type(3)").send_keys("9922883377")


time.sleep(4)
driver.close()