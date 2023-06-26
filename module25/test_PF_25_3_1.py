# run test:
# cd module25
# python -m pytest -v --driver Chrome test_PF_25_3_1.py

from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def login():
   # pytest.driver = webdriver.Chrome('E:\Project\Python\skillfactory\drivers\chromedriver.exe')
   pytest.driver = webdriver.Chrome('..\drivers\chromedriver.exe')
   # Устанавливаем разрешение экрана для браузера. На маленьком разрешении нет кнопки Мои питомцы
   pytest.driver.set_window_size(1400, 1000)

   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')
   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys('test@qiott.com')
   sleep(1)

   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys("Qwerty_123")
   sleep(1)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   sleep(1)

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"


   yield

   pytest.driver.quit()

def test_open_my_pets_page():
   pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
   assert pytest.driver.current_url == "https://petfriends.skillfactory.ru/my_pets"


