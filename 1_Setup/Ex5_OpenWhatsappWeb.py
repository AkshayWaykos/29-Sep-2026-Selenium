import time

print("====Open WhatsApp webapplication==================")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://www.google.com")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="ti6dpd"]').send_keys("AkshayKumar")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/form/div[1]/div/div[1]/div[2]/div[3]/button/div[2]').click()
time.sleep(2)
print(driver.title)
driver.quit()