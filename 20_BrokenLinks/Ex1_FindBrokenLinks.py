from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Edge()
driver.get("https://demoqa.com/broken")

#Step1: Find all links on the page
allLinks = driver.find_elements(By.TAG_NAME, "a")


for link in allLinks:
#Step 2. Get the href attribute of each link
   url = link.get_attribute("href")
   if url is None or url == "":
       continue
   try:
#Step 3: Send a request to the URL and check the status code
       response = requests.get(url)

#Step 4: If the status code is 400 or greater, print that the link is broken
       if response.status_code >= 400:
           print(f"Broken link: {url} --> {response.status_code}")
       else:
           print(f"Valid link: {url}")
   except:
       print(f"Error checking: {url}")
driver.quit()
