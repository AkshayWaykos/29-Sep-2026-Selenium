from selenium.webdriver.common.by import By

class SwageLoginAppl:
    __UserName="//input[@id='user-name']"
    __Password="//input[@id='password']"
    __LoginBtn="//input[@id='login-button']"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,UserVal):
        self.driver.find_element(By.XPATH,self.__UserName).send_keys(UserVal)

    def enter_password(self,Passval):
        self.driver.find_element(By.XPATH,self.__Password).send_keys(Passval)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.__LoginBtn).click()

