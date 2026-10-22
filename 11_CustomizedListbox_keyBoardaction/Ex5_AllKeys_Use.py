import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


firstName=driver.find_element(By.XPATH,"//input[@id='name']")
firstName.send_keys("Waykos@gmail.com")
time.sleep(2)
firstName.send_keys(Keys.CONTROL + "a")

firstName.send_keys(Keys.CONTROL + "x")

email=driver.find_element(By.XPATH,"//input[@id='email']").send_keys(Keys.CONTROL + "v")

time.sleep(5)
firstName.send_keys(Keys.DELETE)


print("--------------------------")
driver.execute_script("window.scroll(0,900)")
time.sleep(2)

print("--------------------------")
country=driver.find_element(By.XPATH,"//select[@id='colors']")

country.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
country.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
country.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
country.send_keys(Keys.ARROW_UP)
time.sleep(5)

print("-------------------------")

country.send_keys(Keys.HOME)
time.sleep(1)

country.send_keys(Keys.END)
time.sleep(1)
print(country.get_attribute("value"))

print("---------------------------")

time.sleep(1)
driver.close()
