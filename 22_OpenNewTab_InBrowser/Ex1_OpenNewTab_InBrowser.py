import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com")

# Open new tab
driver.execute_script("window.open('')")

#switch to new tab
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.youtube.com/")
print(driver.title)
time.sleep(3)

#switch to main screen
driver.switch_to.window(driver.window_handles[0])
driver.get("https://web.whatsapp.com/")
print(driver.title)


time.sleep(5)
driver.quit()



