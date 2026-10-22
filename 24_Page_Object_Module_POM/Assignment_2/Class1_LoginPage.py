
from selenium.webdriver.common.by import By

class OrangeHrmLoginPage:
    __Username="//input[@name='username']"
    __Password="//input[@type='password']"
    __LoginBtn="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,ValidUN):
        self.driver.find_element(By.XPATH,self.__Username).send_keys(ValidUN)

    def enter_password(self,ValidPW):
        self.driver.find_element(By.XPATH,self.__Password).send_keys(ValidPW)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.__LoginBtn).click()


