import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,2000)")

driver.find_element(By.XPATH,"//input[@id='txtDate']").click()

#Select Year
selectYear=driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
s=Select(selectYear)
s.select_by_visible_text("2028")

#Select Month
selectMonth=driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
s1=Select(selectMonth)
s1.select_by_visible_text("Apr")

#select Date
driver.find_element(By.XPATH,"//a[contains(text(),'23')]").click()

finalDate=driver.find_element(By.XPATH,"//input[@id='txtDate']").get_attribute("value")
print("Selected Date =",finalDate)


time.sleep(2)
driver.close()
