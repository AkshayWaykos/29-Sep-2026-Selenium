import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.flipkart.com/")
time.sleep(8)

#Login Pop-up cancel
driver.find_element(By.XPATH,"//span[text()='✕']").click()
time.sleep(5)

#Enter mobile Details
driver.find_element(By.XPATH,"(//input[@class='nw1UBF v1zwn26'])[1]").send_keys("redmi note 15 mobile")
time.sleep(5)

#Click on SearchButton.
driver.find_element(By.XPATH,"(//button[@title='Search for Products, Brands and More'])[1]").click()
time.sleep(5)

#Check and print Rating& Review of REDMI Note 15 5G
ratingDetails1=driver.find_element(By.XPATH,"(//span[@class='PvbNMB'])[1]").text
print(ratingDetails1)
time.sleep(2)

#Check and print Rating& Review of REDMI Note 15 SE 5G Snapdragon (Crimson Reserve, 128 GB) (6 GB RAM)
ratingDetails2=driver.find_element(By.XPATH,"(//span[@class='PvbNMB'])[6]").text
print(ratingDetails2)



time.sleep(8)
driver.close()

