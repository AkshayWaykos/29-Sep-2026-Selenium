from selenium.webdriver.common.by import By

class LogoOfApplication:
    __logo="//div[@class='app_logo']"

    def __init__(self,driver):
        self.driver=driver

    def getlogo(self):
        actualLogoText=self.driver.find_element(By.XPATH,self.__logo).text
        return actualLogoText

