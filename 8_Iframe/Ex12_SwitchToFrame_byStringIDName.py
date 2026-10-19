import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

time.sleep(4)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

time.sleep(2)
driver.switch_to.frame('iframeResult')

time.sleep(2)

show=driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time.')]")
print(show.text)
time.sleep(2)
driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time.')]").click()

time.sleep(2)
driver.switch_to.default_content()

time.sleep(2)
driver.find_element(By.XPATH,"//a[@id='tryhome']").click()
time.sleep(2)
driver.close()


