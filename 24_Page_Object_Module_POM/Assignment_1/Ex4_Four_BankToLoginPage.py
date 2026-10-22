from selenium.webdriver.common.by import By

class BackToLoginPage:
    __LoginLogo="//div[@class='login_logo']"


    def __init__(self,driver):
        self.driver=driver


    def backToLoginPage(self):
        actloginLogoText=self.driver.find_element(By.XPATH,self.__LoginLogo).text
        return actloginLogoText
