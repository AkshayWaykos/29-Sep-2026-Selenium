import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options

ops=Options()
ops.add_argument("--start-maximized")

driver=webdriver.Edge(options=ops)
driver.get("https://www.youtube.com/")
print(driver.title)

time.sleep(5)
driver.close()


#How to maximize browser at opening time only?
# with the help of Option class and "--start-maximized" parameter we can open browser in maximize stage.