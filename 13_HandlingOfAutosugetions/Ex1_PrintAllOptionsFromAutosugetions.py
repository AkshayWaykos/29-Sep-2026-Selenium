import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.google.com")
time.sleep(5)

driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("realme")

#driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]//li[@class='sbct PZPZlf'][2]")   ---> to select realme 16 pro option form auto sug
time.sleep(5)
autoSuggestionsOptions=driver.find_elements(By.XPATH, "(//ul[@class='G43f7e'])[1]/li")

for eachOption in autoSuggestionsOptions:
    print(eachOption.text)


time.sleep(5)
driver.close()