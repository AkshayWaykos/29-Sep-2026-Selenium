import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,1700)")

driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\Admin\Downloads\New folder\Python-Selenium-Notes.docx")


driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()

time.sleep(5)
driver.close()