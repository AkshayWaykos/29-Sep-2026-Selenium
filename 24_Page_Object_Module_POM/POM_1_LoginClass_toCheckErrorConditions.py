from selenium.webdriver.common.by import By

class SwagLoginApplication:

#1: declare variable/webelements as class variables
    __userName="//input[@id='user-name']"
    __password="//input[@id='password']"
    __loginButton="//input[@id='login-button']"
    __errorMsg="//h3[@data-test='error']"

# 2: create constructor of class to initialize driver
    def __init__(self,driver):
        self.driver=driver

#3: create methods to perform action on webelements

    def enterUserName(self,userVal):
        self.driver.find_element(By.XPATH,self.__userName).send_keys(userVal)

    def enterPassword(self,userPwd):
        self.driver.find_element(By.XPATH,self.__password).send_keys(userPwd)

    def clickLoginBtn(self):
        self.driver.find_element(By.XPATH,self.__loginButton).click()

    def errorMsgText(self):
        actualErrorMsgText=self.driver.find_element(By.XPATH,self.__errorMsg).text
        return actualErrorMsgText
