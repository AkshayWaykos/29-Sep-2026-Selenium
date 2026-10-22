import time
from xml.etree.ElementPath import ops

from selenium import webdriver
from selenium.webdriver.edge.options import Options

# after open browser some allow/cancle notification screen will open to handle that screen we used "--disbale-notifications"

obj=Options()
obj.add_argument("--disable-notifications")

driver=webdriver.Edge(options=obj)
driver.get("https://google.com/")
print(driver.title)

time.sleep(5)
driver.close()