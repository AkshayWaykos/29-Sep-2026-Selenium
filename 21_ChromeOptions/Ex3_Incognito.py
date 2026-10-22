import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options

# FireFox Browser  --> -private

options = webdriver.FirefoxOptions()
options.add_argument("-private")

driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com")
print(driver.title)

# print("====================================")
#
# #  Edge Browser ---> --inprivate
#
# options = Options()
# options.add_argument("--inprivate")
#
# driver = webdriver.Edge(options=ops)
# driver.get("https://www.google.com")
# print(driver.title)
#
# print("====================================")
#
# Chrome Browser --->  --incognito
# ops=Options
# ops.add_argument("--incognito")
#
# driver=webdriver.Chrome(options=ops)
# driver.get("https://www.youtube.com/")
# print(driver.title)


time.sleep(5)
driver.close()

# FireFox Browser  -->  -private
# Edge Browser    -->   --inprivate
# Chrome Browser --->   --incognito
