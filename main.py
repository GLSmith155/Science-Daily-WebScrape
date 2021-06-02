import os
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
import time

driver.get("https://www.sciencedaily.com/")
print(driver.title)

search = driver.find_element_by_name("keyword")

search.send_keys(Keys.RETURN)

search = driver.find_element_by_name("keyword")
search.send_keys("heart")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
