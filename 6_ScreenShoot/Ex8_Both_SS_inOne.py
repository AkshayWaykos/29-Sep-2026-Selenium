import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='search_query']").send_keys("Lalbaghcha Raja")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@title='Search']").click()
time.sleep(2)
#full screen
driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\YT17Oct26_03.png")
print("Full Page ScreenShot Saved")
time.sleep(2)

#Special Element
logo=driver.find_element(By.XPATH,"//yt-icon[@id='logo-icon']")
logo.screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\YT17Oct26_04.png")
print("Logo ScreenShot Saved")

time.sleep(2)
driver.close()