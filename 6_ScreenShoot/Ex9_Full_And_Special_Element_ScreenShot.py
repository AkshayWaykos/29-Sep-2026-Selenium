import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")
time.sleep(5)
driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\Oct18_01.png")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='search_query']").send_keys("tv9 marathi live")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@title='Search']").click()
time.sleep(8)
driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\Oct18_02.png")
time.sleep(5)
driver.execute_script("window.scrollTo(0,600)")
time.sleep(5)
driver.find_element(By.XPATH,"//yt-formatted-string[contains(text(),'TV9 Marathi')]").click()
time.sleep(2)
logo=driver.find_element(By.XPATH,"//div[@class='ytSpecAvatarShapeLiveRing']")
logo.screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\Oct18_03.png")
time.sleep(5)
driver.close()