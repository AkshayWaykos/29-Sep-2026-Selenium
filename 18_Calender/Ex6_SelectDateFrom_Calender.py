import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://demoqa.com/date-picker")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='datePickerMonthYearInput']").click()
time.sleep(2)

#select Year
selectYear=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
s1=Select(selectYear)
s1.select_by_visible_text("2027")

#Select Month
selectMonth=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
s2=Select(selectMonth)
s2.select_by_visible_text("April")

#select Date
selectedDate=driver.find_element(By.XPATH,"//div[text()='23']")
print(selectedDate.text)
selectedDate.click()


time.sleep(4)
driver.close()

