# run test:
# python -m pytest -v --driver Chrome --driver-path test1.py

from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('\drivers\chromedriver.exe')
    pytest.driver.set_window_size(1400, 1000)

    # Переходим на страницу авторизации
    pytest.driver.get('https://www.wildberries.ru/')

    yield

    pytest.driver.quit()


def test_search_fruto_nyanya():

    pytest.driver.implicitly_wait(10)
    # WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located
    sleep(3)
    search = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located((By.ID, "searchInput")))
    query_text = 'фруктовое пюре в мягкой упаковке фрутоняня'
    search.send_keys(query_text)
    search.send_keys(Keys.RETURN)
    sleep(5)
    assert pytest.driver.find_element(By.TAG_NAME, "h1").text == f"По запросу «{query_text}» найдено"




    # footer = pytest.driver.find_element(By.TAG_NAME, "footer")
    # scroll_origin = ScrollOrigin.from_element(footer, 0, -50)
    # ActionChains(pytest.driver) \
    #     .scroll_from_origin(scroll_origin, 0, 200) \
    #     .perform()

    # prices = pytest.driver.find_elements(By.CLASS_NAME, "price__lower-price")
    # print(len(prices))
    # price_list = []
    # for el in prices:
    #     price_list.append(el.text)
    #
    # print(price_list)



