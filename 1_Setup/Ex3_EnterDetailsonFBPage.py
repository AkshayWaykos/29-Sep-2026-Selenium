import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.facebook.com")
print(driver.title)
time.sleep(4)

driver.find_element(By.XPATH,'//*[@id="_R_c9l6neappb6amH1_"]').send_keys("Abcd@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="_R_cdl6neappb6amH1_"]').send_keys("12345")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div[2]/form/div/div[1]/div/div[3]/div/div/div').click()

print("FB page try to Login Successfully")
driver.quit()