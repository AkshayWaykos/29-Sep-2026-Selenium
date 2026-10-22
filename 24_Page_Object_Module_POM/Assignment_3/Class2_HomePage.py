
from selenium.webdriver.common.by import By

class HomePage:
    __OpenNewAcc="//a[@href='openaccount.htm']"
    __AccType="//option[contains(text(),'SAVINGS')]"
    __ExistingAcc="//option[contains(text(),'13344')]"
    __NewAccBtn="//input[@class='button']"
    __AccNoText="/html/body/div[1]/div[3]/div[2]/div/div[2]/p[2]"

    def __init__(self,driver):
        self.driver=driver

    def select_Acc(self):
        self.driver.find_element(By.XPATH,self.__OpenNewAcc).click()

    def select_AccType(self):
        self.driver.find_element(By.XPATH,self.__AccType).click()

    def select_ExistingAcc(self):
        self.driver.find_element(By.XPATH,self.__ExistingAcc).click()

    def click_AccOpenBtn(self):
        self.driver.find_element(By.XPATH,self.__NewAccBtn).click()

    def getAccNoText(self):
        show=self.driver.find_element(By.XPATH,self.__AccNoText).text
        print(show)

