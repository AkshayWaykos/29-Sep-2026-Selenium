import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
time.sleep(2)
driver.get("https://www.makemytrip.com/")
time.sleep(7)

#Closed Login Pop-up Window
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()

#click on Departure
driver.find_element(By.XPATH,"//span[text()='Departure']").click()
time.sleep(5)

expMonth="April 2027"
expDate="23"

while True:
    actMonth=driver.find_element(By.XPATH,"//div[@class='DayPicker-Caption']").text
    if actMonth==expMonth:
        break
    else:
        #click On Next Button
        driver.find_element(By.XPATH,"//span[@aria-label='Next Month']").click()
        time.sleep(2)

#select Date
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='dateInnerCell']//p[text()='"+expDate+"'])[1]").click()

time.sleep(5)
driver.close()


