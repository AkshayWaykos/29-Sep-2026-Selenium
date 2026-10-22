import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.google.com/")
time.sleep(8)

driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("AkshayKumar")

time.sleep(8)
allOptionsFromSuggestion=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]//li")
print(len(allOptionsFromSuggestion))

time.sleep(8)
for eachOptionFromSugg in allOptionsFromSuggestion:
    textVal=eachOptionFromSugg.text
    print(textVal)

time.sleep(5)
driver.close()
