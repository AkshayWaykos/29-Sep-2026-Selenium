import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.guru99.com/test/delete_customer.php")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("112233")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='submit']").click()

time.sleep(2)
pop_up=driver.switch_to.alert
print(pop_up.text)

time.sleep(2)
pop_up.dismiss()

time.sleep(2)
driver.close()