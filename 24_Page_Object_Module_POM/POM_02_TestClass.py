import time

from selenium import webdriver
from POM_01_Login_and_Home_Page import SwagLoginPage
from selenium.webdriver.common.by import By


driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

loginPageObj=SwagLoginPage(driver)

loginPageObj.enterUN("standard_user")

loginPageObj.enterPwd("secret_sauce")

loginPageObj.clikcbutton()

actLogoText=loginPageObj.homePageLogo(driver)
exptLogoText="Swag Labs"

if actLogoText==exptLogoText:
    print("Login Test is Passed")
else:
    print("Login Test is Failed")

time.sleep(4)
driver.close()