# By.ID
# By.NAME
# By.XPATH
# By.CLASS_NAME
# By.TAG_NAME
# By.LINK_TEXT
# By.PARTIAL_LINK_TEXT

# By.CSS_SELECTOR

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('https://testautomationpractice.blogspot.com/')

# By.ID -->
time.sleep(2)
driver.find_element(By.ID,'name').send_keys("Akshay")
print("By.ID Locator executed")
print("-----------------------------------------------")

# By.NAME -->
time.sleep(2)
text1=driver.find_element(By.NAME,'BookTable').text
print(text1)
print("By.Name Locator executed")

print("-----------------------------------------------")

# By.XPATH -->
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="phone"]').send_keys("9988776655")
print("By.XPATH Locator Executed")

print("-----------------------------------------------")
# By.CLASS_NAME
time.sleep(2)
driver.find_elements(By.CLASS_NAME,'form-control')[1].send_keys("abc@gmal.com")
print("By.CLASS_NAME Locator Executed")

print("-----------------------------------------------")
# By.TAG_NAME
time.sleep(2)
driver.get("file:///C:/Users/Admin/PycharmProjects/29-Sep-2026-Selenium/3_HTML/Ex8_tagname_name_id.html")
driver.find_element(By.TAG_NAME,"input").send_keys("Akshay")
print("By.TAG_NAME Locator Executed")
print("-----------------------------------------------")
# By.LINK_TEXT
driver.get("file:///C:/Users/Admin/PycharmProjects/29-Sep-2026-Selenium/3_HTML/Ex9_LinkText.html")
driver.find_element(By.LINK_TEXT,"FaceBook").click()
print("By.LINK_TEXT Locator Executed")
print("-----------------------------------------------")
# By.PARTIAL_LINK_TEXT
driver.get("file:///C:/Users/Admin/PycharmProjects/29-Sep-2026-Selenium/3_HTML/Ex9_LinkText.html")
driver.find_element(By.PARTIAL_LINK_TEXT,"Face").click()
print("By.PARTIAL_LINK_TEXT Locator Executed")
print("-----------------------------------------------")


driver.close()