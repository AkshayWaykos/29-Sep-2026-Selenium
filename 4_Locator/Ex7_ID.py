import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()

driver.get("file:///C:/Users/Admin/PycharmProjects/29-Sep-2026-Selenium/3_HTML/Ex8_tagname_name_id.html")

#Enter FN name with tag name
driver.find_element(By.ID,"1234").send_keys("Akshay")

#Enter LN name with tag name
driver.find_element(By.ID,"5678").send_keys("Sagar")

time.sleep(2)