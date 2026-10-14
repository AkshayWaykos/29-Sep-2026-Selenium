import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
HeadlingSS=driver.find_element(By.XPATH,"//h1[@class='title']")
HeadlingSS.screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\specificScreenS2.png")

driver.close()