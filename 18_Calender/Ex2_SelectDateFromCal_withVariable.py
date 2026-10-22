import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://demoqa.com/date-picker")

#Click on field
driver.find_element(By.XPATH,"//input[@id='datePickerMonthYearInput']").click()

yearVal="2028"
monthVal="April"
dateVal="23"


#Select Year From Year Drop-down
year=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
s1=Select(year)
s1.select_by_visible_text(yearVal)

#Select Month From Month Drop-down
month=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
s2=Select(month)
s2.select_by_visible_text(monthVal)

#select Date From Date filed (Concatenation)
driver.find_element(By.XPATH,"//div[contains(text(),'"+dateVal+"')]").click()

#Get Date After Selected.
time.sleep(5)
showDate=driver.find_element(By.XPATH,"//input[@id='datePickerMonthYearInput']").get_attribute("value")
print("Selected Date =",showDate)


time.sleep(5)
driver.close()