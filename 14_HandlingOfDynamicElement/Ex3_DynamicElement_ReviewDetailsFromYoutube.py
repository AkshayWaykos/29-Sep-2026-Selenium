import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@name='search_query']").send_keys("JayShreeRam")
time.sleep(5)

driver.find_element(By.XPATH,"//button[@title='Search']").click()
time.sleep(5)

viewcount=driver.find_element(By.XPATH,"(//div[@id='metadata'])[2]").text
print(viewcount)


time.sleep(5)
