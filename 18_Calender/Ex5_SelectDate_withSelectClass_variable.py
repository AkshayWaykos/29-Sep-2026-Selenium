import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,1300)")

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

expectMonth="April"
expectYear ="2027"
expDate="23"

while True:
    actMonth=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    actYear=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if actMonth == expectMonth and actYear == expectYear:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        time.sleep(2)

#select date
driver.find_element(By.XPATH,"//a[text()='"+expDate+"']").click()

time.sleep(4)
driver.close()