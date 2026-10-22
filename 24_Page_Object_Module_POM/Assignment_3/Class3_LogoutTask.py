
from selenium.webdriver.common.by import By

class Logout:
    __logoutApp="//a[@href='logout.htm']"

    def __init__(self,driver):
        self.driver=driver

    def click_logoutBtn(self):
        self.driver.find_element(By.XPATH,self.__logoutApp).click()

