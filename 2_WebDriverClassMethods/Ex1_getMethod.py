import time

print("===Webdriver method -> Get Method===")

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com/")

time.sleep(2)
