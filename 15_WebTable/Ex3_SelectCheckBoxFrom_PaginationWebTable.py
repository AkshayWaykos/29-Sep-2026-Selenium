#5: In Pagination WebTable  -> select checkbox of name table
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
driver.execute_script("window.scroll(0,2500)")

time.sleep(5)
checkBox=driver.find_element(By.XPATH,"//table[@id='productTable']//tr[2]/td[4]/input")
checkBox.click()

time.sleep(5)
driver.close()