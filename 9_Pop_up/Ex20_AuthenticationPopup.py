import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Firefox()
# driver.get("https://the-internet.herokuapp.com/basic_auth")

time.sleep(5)

driver.get("https://admin:dmin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)