import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()

driver.get("file:///C:/Users/Admin/PycharmProjects/29-Sep-2026-Selenium/3_HTML/Ex9_LinkText.html")

#Enter FN name with tag name
driver.find_element(By.LINK_TEXT,"FaceBook").click()

time.sleep(2)