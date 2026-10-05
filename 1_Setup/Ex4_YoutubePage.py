import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/div/div/form/input').send_keys("Tv9 Marathi")
driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/div/button').click()
time.sleep(2)

os.makedirs("ScreenShoot", exist_ok=True)
driver.save_screenshot("ScreenShoot/youtube_search.png")

print(driver.title)
time.sleep(4)
driver.quit()

