import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Firefox()
driver.get("https://www.google.com")

#Open to new Tab
driver.execute_script("window.open('')")

#switch to new Tab
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.youtube.com/")
print(driver.title)
time.sleep(4)

driver.execute_script("window.open('')")
#Switch to 2 tab
driver.switch_to.window(driver.window_handles[2])
driver.get("https://web.whatsapp.com/")
print(driver.title)
time.sleep(4)

driver.execute_script("window.open('')")
#Switch to 3 tab
driver.switch_to.window(driver.window_handles[3])
driver.get("https://www.facebook.com/")
print(driver.title)
time.sleep(4)

#switch to 1 tab and search abcd song
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//input[@name='search_query']").send_keys("ABCD Song")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@title='Search']").click()
time.sleep(10)

driver.quit()