import time

from selenium import webdriver
from POM1_Login import SwagLoginApplication
from POM2_Home import SwagHomePage


driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")


loginObj=SwagLoginApplication(driver)       #create Object of SwagLoginApplication class

loginObj.enterUserName("standard_user")      #Sent Value for enterUserName method
time.sleep(2)
loginObj.enterPassword("secret_sauce")      #Sent Value for enterPassword method
time.sleep(2)
loginObj.clickLoginBtn()
time.sleep(2)

print("-----------------------------------")


logo=SwagHomePage(driver)
actLogoText=logo.getLogoText()
expLogoText="Swag Labs"

if actLogoText==expLogoText:
    print("Login Test is Passed")
else:
    print("Login Test is Failed")

time.sleep(5)
driver.close()