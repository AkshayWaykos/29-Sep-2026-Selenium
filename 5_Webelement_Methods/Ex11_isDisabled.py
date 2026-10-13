import time
from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.instagram.com/")

result=driver.find_element(By.XPATH,"//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft']").is_selected()
print(result)

if result:
    print("Button is Enabled")
else:
    print("Button is Disabled")