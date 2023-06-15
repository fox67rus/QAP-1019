from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
assert "Python" in driver.title
elem  = driver.find_element(By.NAME, "q")
elem.clear()
# 12:35