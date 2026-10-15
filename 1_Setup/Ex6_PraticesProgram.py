import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from websocket import send

driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Akshay")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("akki@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9988774433")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("LIG 425 KPHB phase 7th Hyderabad")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='male']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='sunday']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//select[@id='country']/option[4]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//select[@id='colors']/option[6]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//select[@id='animals']/option[5]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys('07/10/2026')
time.sleep(2)
driver.find_element(By.XPATH,"//a[@data-date='8']").click()
time.sleep(2)

start_Date=driver.find_element(By.ID,"start-date")
end_Date=driver.find_element(By.ID,"end-date")

driver.execute_script("arguments[0].value='2026-10-28'",start_Date)
driver.execute_script("arguments[0].value='2026-12-15'",end_Date)
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()
time.sleep(2)


driver.close()