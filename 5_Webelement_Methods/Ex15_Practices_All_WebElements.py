import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# send_keys()
# clear()
# click()
# text
# get_attribute
# is_enabled
# is_selected
# is_displayed

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("AKSHAY")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").clear()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("AKSHAY")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name']").get_attribute('placeholder')

time.sleep(2)

result1 =driver.find_element(By.XPATH,"//button[@class='start']").is_enabled()
print(result1)
time.sleep(2)
result2=driver.find_element(By.XPATH,"//input[@id='female']").is_selected()
print(result2)
time.sleep(2)
result3=driver.find_element(By.XPATH,"//h2[contains(text(),'Tabs')]").is_displayed()
print(result3)
time.sleep(2)

driver.close()