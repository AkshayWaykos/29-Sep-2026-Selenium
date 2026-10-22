from selenium.webdriver.common.by import By

class SwagLoginPage:
#Declare Variables with value
    __userName="//input[@id='user-name']"
    __password="//input[@id='password']"
    __LogButton="//input[@id='login-button']"
    __logoText="//div[@class='app_logo']"

#Constructor
    def __init__(self,driver):
        self.driver=driver

#Create Method
    def enterUN(self,userVal):
        self.driver.find_element(By.XPATH,self.__userName).send_keys(userVal)

    def enterPwd(self,pwdVal):
        self.driver.find_element(By.XPATH,self.__password).send_keys(pwdVal)

    def clikcbutton(self):
        self.driver.find_element(By.XPATH,self.__LogButton).click()

    def homePageLogo(self,logo):
        actLogoText=self.driver.find_element(By.XPATH,self.__logoText).text
        return actLogoText



