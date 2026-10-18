import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("file:///C:/Users/Admin/PycharmProjects/29-Sep-2026-Selenium/3_HTML/Ex11_UseToHandleCaptcha.html")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='text'][1]").send_keys("Akshay")

time.sleep(2)
copyValue = driver.find_element(By.XPATH, "//input[@type='text'][1]").get_attribute("value")

driver.find_element(By.XPATH,"//input[@type='text'][2]").send_keys(copyValue)


print("copy in to to B")
time.sleep(2)

driver.close()


