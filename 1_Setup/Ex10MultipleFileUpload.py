import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scroll(0,1700)")

#2 File Path check and Save in object
file1=r"C:\Users\Admin\Downloads\New folder\Python-Selenium-Notes.docx"
file2=r"C:\Users\Admin\Downloads\New folder\Assignment2-AkshayWaykos.txt"

#check ID for Multiple File Upload
multipleFileUploadButton=driver.find_element(By.ID,"multipleFilesInput")

#attached 2 Path in send Key
multipleFileUploadButton.send_keys(f"{file1}\n{file2}")
#multi_input.send_keys(f"{file1}\n{file2}")

#click on Upload Multiple file Button
twoFileUpload=driver.find_element(By.XPATH,"//button[text()='Upload Multiple Files']")
print(twoFileUpload.text)
twoFileUpload.click()

time.sleep(5)
driver.close()