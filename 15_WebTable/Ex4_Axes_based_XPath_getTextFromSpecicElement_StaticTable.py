import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
driver.execute_script("window.scroll(0,2100)")

system=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='System']//parent::tr/td[2]").text
print(system)
time.sleep(4)

networkSpeedOfChrome=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='Chrome']//parent::tr/td[contains(text(),'Mbps')]").text
print(networkSpeedOfChrome)
time.sleep(4)

cpuValueOfFirefox=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='Firefox']//parent::tr/td[contains(text(),'%')]").text
print(cpuValueOfFirefox)
time.sleep(4)

mbsValu=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='Internet Explorer']//parent::tr//td[contains(text(),'MB/s')]").text
print(mbsValu)


time.sleep(8)
driver.close()