# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#     for Firefox:
#     https://github.com/mozilla/geckodriver/releases
#  2) Install all requirements:
#     pip install pytest-selenium
#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path drivers\chromedriver.exe test_selenium_simple.py
#     python -m pytest -v --driver Chrome --driver-path C:\webdrivers\chromedriver.exe test_selenium_simple.py
#     or
#     python pytest --driver Firefox --driver-path drivers\geckodriver.exe test_selenium_simple.py


import time
from selenium.webdriver.common.by import By


def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')

    time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    # search_input = selenium.find_element_by_name('q')
    search_input = selenium.find_element(By.NAME, 'q')

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test selenium')

    time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    # search_button = selenium.find_element_by_name("btnK")
    search_button = selenium.find_element(By.NAME, 'btnK')
    # search_button.click()
    search_button.submit()

    time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')
    selenium.quit()