from selenium.webdriver.common.by import By

class ParaBankLoginPage:
    __Username="//input[@name='username']"
    __Password="//input[@name='password']"
    __LogInBtn="//input[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,userVal):
        self.driver.find_element(By.XPATH,self.__Username).send_keys(userVal)

    def enter_password(self,passwordVal):
        self.driver.find_element(By.XPATH,self.__Password).send_keys(passwordVal)

    def click_LogInBtn(self):
        self.driver.find_element(By.XPATH,self.__LogInBtn).click()


