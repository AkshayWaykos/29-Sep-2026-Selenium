import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scroll(0,900)")
time.sleep(5)
pointMe=driver.find_element(By.XPATH,"//button[contains(text(),'Point Me')]")

act=ActionChains(driver)

act.move_to_element(pointMe).perform()


time.sleep(5)
laptopOption=driver.find_element(By.XPATH,"//a[contains(text(),'Laptops')]")
print(laptopOption.text)
laptopOption.click()


time.sleep(5)
driver.close()


