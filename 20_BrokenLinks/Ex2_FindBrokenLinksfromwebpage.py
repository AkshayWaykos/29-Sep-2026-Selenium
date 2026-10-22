from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Edge()
driver.get("https://demoqa.com/broken")

# Saare <a> tag pakdo
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    url = link.get_attribute("href")

    if url:  # Agar link khaali nahi hai toh hi check karo
        try:
            res = requests.get(url, timeout=5)
            if res.status_code >= 400:
                print(f"BROKEN -> {url} | Code: {res.status_code}")
            else:
                print(f"OK -> {url}")
        except:
            print(f"ERROR -> {url}")

driver.quit()