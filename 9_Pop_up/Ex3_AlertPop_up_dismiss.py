import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("http://demo.guru99.com/test/delete_customer.php")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("1234")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='submit']").click()

time.sleep(2)
alt=driver.switch_to.alert
print(alt.text)

time.sleep(2)
alt.dismiss()

time.sleep(2)
driver.close()




