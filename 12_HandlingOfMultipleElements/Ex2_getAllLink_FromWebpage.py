import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://autotestsandbox.com/examples/nested-iframes")

allLinkOfWebpage=driver.find_elements(By.XPATH,"//a")
print(len(allLinkOfWebpage))

for eachLink in allLinkOfWebpage:
    print(eachLink.text)

time.sleep(4)
driver.close()

