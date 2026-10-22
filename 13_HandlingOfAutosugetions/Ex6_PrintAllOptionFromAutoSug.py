import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com")

driver.find_element(By.XPATH,"//input[@name='search_query']").send_keys("mahabharat")

time.sleep(3)
allOptions=driver.find_elements(By.XPATH,"//div[@id='i0']//span")

count = len(allOptions)
print(count)

for eachOptions in allOptions:
    print(eachOptions.text)


time.sleep(2)
driver.close()


