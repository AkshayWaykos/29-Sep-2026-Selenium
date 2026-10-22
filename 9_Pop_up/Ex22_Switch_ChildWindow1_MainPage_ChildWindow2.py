import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://skpatro.github.io/demo/links/")

time.sleep(5)
NewTab=driver.find_element(By.XPATH,"//input[@name='NewTab']")
print(NewTab.text)
NewTab.click()

time.sleep(5)
firstScreen1=driver.window_handles
driver.switch_to.window(firstScreen1[1])

time.sleep(8)
word=driver.find_element(By.XPATH,"(//span[text()='Training'])[1]")
print(word.text)
word.click()

#back to main screen
driver.switch_to.window(firstScreen1[0])

print("-------------Below code for Second Screen-------------------------------")

time.sleep(5)
newWindow=driver.find_element(By.XPATH,"//input[@name='NewWindow']")
print(newWindow.text)
newWindow.click()

time.sleep(10)
firstScreen2=driver.window_handles
driver.switch_to.window(firstScreen2[2])

time.sleep(5)
driver.maximize_window()

time.sleep(5)
home=driver.find_element(By.XPATH,"(//span[contains(text(),'HOME')])[1]")
print(home.text)
home.click()

time.sleep(5)
driver.switch_to.window(firstScreen2[0])

time.sleep(5)
driver.close()