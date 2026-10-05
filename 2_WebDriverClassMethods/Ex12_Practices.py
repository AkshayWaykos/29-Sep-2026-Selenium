import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.google.com/")
time.sleep(4)
driver.get('https://www.facebook.com/')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="_R_c9l6neappb6amH1_"]').send_keys("abcd@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="_R_cdl6neappb6amH1_"]').send_keys("1234")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div[2]/form/div/div[1]/div/div[3]/div/div/div').click()
print(driver.title)
time.sleep(2)
print(driver.current_url)
time.sleep(2)
driver.close()
