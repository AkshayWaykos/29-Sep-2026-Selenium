import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")
time.sleep(4)

driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\FullSShot1.png")
time.sleep(4)


driver.get("https://testautomationpractice.blogspot.com/")
driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\FullSShot2.png")

driver.close()