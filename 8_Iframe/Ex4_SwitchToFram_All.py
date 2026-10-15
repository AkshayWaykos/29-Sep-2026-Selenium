import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
# print("Fist Enter in iFram")
# driver.find_element(By.XPATH,"//button[@type='button']").click()
# print("Click on iframe button")

print("-------------------------------------")


driver.switch_to.frame(0)
print("through Index Handle 1st iframe")
driver.find_element(By.XPATH,"//button[@type='button']").click()

print("-------------------------------------")

# driver.switch_to.frame("iframeResult")
# print("iFrame handle through ID/string elements")
# driver.find_element(By.XPATH,"//button[@type='button']").click()


time.sleep(2)
driver.close()