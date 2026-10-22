import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://www.google.com/")

#Enter mobile
driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("redmi")
time.sleep(2)

allOptionAddress=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]/li")

expText="redmi note 17"

for eachOptionAddress in allOptionAddress:
    actText=eachOptionAddress.text
    if actText==expText:    #redmi note 17 == redmi note 17
        eachOptionAddress.click()
        break


time.sleep(50)