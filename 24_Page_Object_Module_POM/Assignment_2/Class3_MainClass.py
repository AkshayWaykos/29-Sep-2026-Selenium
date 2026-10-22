import time

from selenium import webdriver
from Class1_LoginPage import OrangeHrmLoginPage
from Class2_LogoutPage import LogoutPage

driver=webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)

#Object Created for Class 1
loginPageObj=OrangeHrmLoginPage(driver)

loginPageObj.enter_username("Admin")
time.sleep(4)
loginPageObj.enter_password("admin123")
time.sleep(4)
loginPageObj.click_login()
time.sleep(4)
print("Login Successfully")

print("-------------------------------")

#Object Created for Class 2

logoutPageObj=LogoutPage(driver)
time.sleep(4)
logoutPageObj.click_UD()
time.sleep(4)
logoutPageObj.click_LO()
time.sleep(5)
print("Logout Successfully")

driver.close()