import time

from selenium import webdriver
from Class1_LoginPage import ParaBankLoginPage
from Class2_HomePage import HomePage
from Class3_LogoutTask import Logout

driver=webdriver.Firefox()
driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

#Login class obj creation & method calls
loginObj=ParaBankLoginPage(driver)
loginObj.enter_username("john")
time.sleep(2)
loginObj.enter_password("demo")
time.sleep(2)
loginObj.click_LogInBtn()
time.sleep(4)

#Home Page obj creation & methods calls

homeObj=HomePage(driver)

homeObj.select_Acc()
time.sleep(2)
homeObj.select_AccType()
time.sleep(4)
homeObj.select_ExistingAcc()
time.sleep(2)
homeObj.click_AccOpenBtn()
time.sleep(2)
homeObj.getAccNoText()
time.sleep(2)

#Logout Page obj creation & methods calls


logout=Logout(driver)
time.sleep(2)
logout.click_logoutBtn()
time.sleep(2)

driver.close()