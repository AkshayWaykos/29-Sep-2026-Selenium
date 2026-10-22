import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(10)

# Search xpath
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("sambata")
time.sleep(5)  # suggestion aane ke liye wait

# To check all Suggestions
all_options = driver.find_elements(By.XPATH, "//div[starts-with(@id,'searchbox-suggestion')]")

expect = 'sambata rap'
print(f"Total options: {len(all_options)}")

for option in all_options:
    # aria-label se text lena best hai YouTube pe
    actual = option.get_attribute("aria-label")
    if actual:
        actual = actual.lower().strip()
        print(actual)

        # == ki jagah 'in' use kar, kyunki 'sambata rap song' me bhi 'sambata rap' hai
        if expect in actual:
            option.click()
            break

time.sleep(5)
driver.close()