import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options

ops=Options()
ops.add_argument("--headless")


driver=webdriver.Edge(options=ops)
driver.get("https://www.youtube.com/")
print(driver.title)

time.sleep(5)
driver.close()


# How we can get the output without opening the browser in selenium?
# with the help of Option class and "--headless" parameter we can execute the program without browser open.