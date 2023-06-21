from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--windows-size=800,600")
options.add_argument("--disable-dev-shm-usage")

driver =  webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
# assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
sleep(1)
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No result found." not in driver.page_source
sleep(2)
new_window = driver.switch_to.new_window()
driver.get("https://ya.ru")
sleep(2)

driver.switch_to.window(driver.window_handles[0])
sleep(2)
driver.refresh()
sleep(1)
driver.close()
sleep(1)
driver.quit()

# 23:43
