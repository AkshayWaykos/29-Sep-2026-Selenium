import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.google.com")
time.sleep(4)
Logo=driver.find_element(By.XPATH,"//div[@class='naW5gc uZekje']")
Logo.screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\LogoPic2.png")
print("LOGO ScreenShoot Taken")
time.sleep(4)

driver.find_element(By.XPATH,"//textarea[@id='ti6dpd']").send_keys("Akshay Waykos" + Keys.ENTER)
time.sleep(4)

#Bcoz of captach below code not executed.
driver.find_element(By.XPATH,"//span[text()='इमेज']").click()
time.sleep(4)

driver.save_screenshot("C:\\Users\\Admin\\PycharmProjects\\29-Sep-2026-Selenium\\6_ScreenShoot\\ScreenShoot\\LogoPic2.png")

time.sleep(2)
driver.close()

