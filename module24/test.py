from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_google():
    driver = webdriver.Chrome()
    driver.get('https://google.com')

    search_input = driver.find_element(By.NAME,'q')
    search_input.clear()
    search_input.send_keys('selenium')
    search_input.submit()
    # search_input.send_keys(Keys.RETURN)
    sleep(2)

    driver.quit()
