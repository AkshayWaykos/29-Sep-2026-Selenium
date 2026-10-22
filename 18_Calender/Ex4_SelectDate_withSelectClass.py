import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,2000)")

driver.find_element(By.XPATH,"//input[@id='txtDate']").click()

time.sleep(4)
year=driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
s1=Select(year)
s1.select_by_visible_text("2028")

time.sleep(4)
month=driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
s2=Select(month)
s2.select_by_visible_text("Apr")

time.sleep(4)
driver.find_element(By.XPATH,"(//a[@class='ui-state-default'])[23]").click()

selectedDate=driver.find_element(By.XPATH,"//input[@id='txtDate']").get_attribute("value")
print("Final Selected Date =",selectedDate)


time.sleep(4)
driver.close()


