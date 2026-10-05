import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()

driver.get("https://www.programiz.com/java-programming/online-compiler/")
time.sleep(4)
driver.find_element(By.XPATH,"/html/body/div[2]/div[7]/div[4]/div[1]/a[1]").click()
time.sleep(4)
editor = driver.find_element(By.CSS_SELECTOR,".cm-content")
editor.click()
time.sleep(2)
editor.send_keys(Keys.CONTROL + "a")
editor.send_keys(Keys.DELETE)
time.sleep(2)
editor.send_keys("print('Hi Akshay')")
time.sleep(2)
if os.path.exists("ScreenShoot/java_compiler.png"):
    os.remove("ScreenShoot/java_compiler.png")
os.makedirs("ScreenShoot",exist_ok=True)
driver.save_screenshot("Screen01102026/java_compiler.png")
time.sleep(2)

driver.quit()
