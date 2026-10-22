from selenium.webdriver.common.by import By


class LogoutApplication:
    __Hamburger="//button[@id='react-burger-menu-btn']"
    __Logout="//a[@id='logout_sidebar_link']"

    def __init__(self,driver):
        self.driver=driver

    def click_humbuger(self):
        self.driver.find_element(By.XPATH,self.__Hamburger).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.__Logout).click()



