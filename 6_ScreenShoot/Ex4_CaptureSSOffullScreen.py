from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\FullScreenShoot2.png")
print("ScreenShoot Taken")
driver.close()