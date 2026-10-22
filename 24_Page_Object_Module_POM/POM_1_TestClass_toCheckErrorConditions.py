import time

from selenium import webdriver
from POM_1_LoginClass_toCheckErrorConditions import SwagLoginApplication

driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

loginObj=SwagLoginApplication(driver)       #create Object of SwagLoginApplication class

loginObj.enterUserName("wrong_UserName")      #Sent Value for enterUserName method
time.sleep(2)
loginObj.enterPassword("wrong_pwd")      #Sent Value for enterPassword method
time.sleep(2)
loginObj.clickLoginBtn()
time.sleep(2)

actualErrorMsgText=loginObj.errorMsgText()
exptErrorMsgText="Epic sadface: Username and password do not match any user in this service"

if actualErrorMsgText==exptErrorMsgText:
    print("Login Failed Test is Passed")
else:
    print("Login Failed Test is Failed")

time.sleep(4)
driver.close()