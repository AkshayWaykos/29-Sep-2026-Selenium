import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("alkhni ranjan")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@title='Search']").click()

links=driver.find_elements(By.XPATH,"//a")

print(len(links))

for eachLinks in links:
    print(eachLinks.text)

time.sleep(5)
driver.close()