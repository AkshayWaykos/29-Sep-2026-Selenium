import time
from selenium import webdriver
from Ex1_First_LoginPageClass import SwageLoginAppl
from Ex2_Second_HomePageClass import LogoOfApplication
from Ex3_Thrid_LogoutPageClass import LogoutApplication
from Ex4_Four_BankToLoginPage import BackToLoginPage

driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")


#Objection creation of SwageLoginAppl
loginObj=SwageLoginAppl(driver)

loginObj.enter_username("standard_user")
time.sleep(2)
loginObj.enter_password("secret_sauce")
time.sleep(2)
loginObj.click_login()
time.sleep(5)

print("-------------------------------------")
#Objection creation of LogoOfApplication

logoObj=LogoOfApplication(driver)
actualLogoText=logoObj.getlogo()
exp_logoText = "Swag Labs"

if actualLogoText == exp_logoText:
    print("Logo Of Application Is proper")
else:
    print("Logo Of Application is mismatch")

print("-------------------------------------")

#Object creation of LogoutApplication

logout=LogoutApplication(driver)

logout.click_humbuger()
time.sleep(2)
logout.click_logout()

print("-------------------------------------")

loginObj=BackToLoginPage(driver)

actloginLogoText=loginObj.backToLoginPage()
exploginLogoText="Swag Labs"

if actloginLogoText==exploginLogoText:
    print("Proper Logo text of Login Screen")
else:
    print("Mismatch of Login screen Logo Text.")


time.sleep(5)
driver.close()
