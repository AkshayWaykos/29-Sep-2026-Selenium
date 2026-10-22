import time

from cffi.cparser import CDEF_SOURCE_STRING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Edge()
driver.get("http://watir.com/examples/shadow_dom.html")
time.sleep(2)

driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Akshay")

time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()


time.sleep(4)
driver.close()