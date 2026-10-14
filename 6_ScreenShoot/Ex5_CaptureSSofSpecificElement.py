import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")
time.sleep(5)
SSY=driver.find_element(By.XPATH,"//yt-icon[@id='logo-icon']")
SSY.screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\yticon1.png")
print("Icon ScreenShoot Taken")

time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='search_query']").send_keys("sambata rap song")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@title='Search']").click()
time.sleep(5)
driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\sambataSinger1.png")
time.sleep(5)
print("Sambata youtube page ScreenShoot Taken")
driver.close()