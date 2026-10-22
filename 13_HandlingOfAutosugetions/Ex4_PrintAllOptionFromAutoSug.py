import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")

time.sleep(8)
driver.find_element(By.XPATH,"//input[@class='ytSearchboxComponentInput yt-searchbox-input title']").send_keys("alakh niranjan aadesh")

time.sleep(8)
autoSuggestionsOptions=driver.find_elements(By.XPATH,"//div[@id='i0']")
time.sleep(5)
count=len(autoSuggestionsOptions)
print(count)

for eachAutoSugOptions in autoSuggestionsOptions:
    print(eachAutoSugOptions.text)



time.sleep(5)
driver.close()
