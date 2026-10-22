import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options

#It uses to Zome in/out the browser screen.

Obj=Options()
Obj.add_argument("--force-device-scale-factor=1")

driver=webdriver.Edge(options=Obj)
driver.get("https://google.com/")
print(driver.title)

time.sleep(5)
driver.close()