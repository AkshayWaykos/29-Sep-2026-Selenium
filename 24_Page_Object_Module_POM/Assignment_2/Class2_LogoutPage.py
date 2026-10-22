from selenium.webdriver.common.by import By
class LogoutPage:
    __userdropdown="//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    __logutOption="//a[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver=driver

    def click_UD(self):
        self.driver.find_element(By.XPATH,self.__userdropdown).click()

    def click_LO(self):
        self.driver.find_element(By.XPATH,self.__logutOption).click()

