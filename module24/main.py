from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
url = "https://my-calend.ru/magnitnye-buri"
driver.get(url)


driver.quit()

