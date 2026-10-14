import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")
time.sleep(4)
SpecificScreen1=driver.find_element(By.XPATH, "//div[@id='content-wrapper']")
SpecificScreen1.screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\YTScreeen1.png")
print("Title ScreenShoot Take from Youtube")
time.sleep(4)

SpecificScreen2=driver.find_element(By.XPATH,"//a[@title='Home']")
SpecificScreen2.screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\YTScreeen2.png")
print("Home icon ScreenShoot Take from Youtube")

time.sleep(4)
driver.find_element(By.XPATH,"//input[@name='search_query']").send_keys("Emiway Bantai")
driver.find_element(By.XPATH,"//button[@title='Search']").click()

time.sleep(4)

driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\YTScreeen3.png")

driver.close()