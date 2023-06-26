# run test:
# cd module25
# python -m pytest -v --driver Chrome --driver-path ..\drivers\chromedriver.exe test_PF_25_3.py
# python -m pytest -v --driver Chrome test_PF_25_3.py

from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
   # pytest.driver = webdriver.Chrome('E:\Project\Python\skillfactory\drivers\chromedriver.exe')
   pytest.driver = webdriver.Chrome('..\drivers\chromedriver.exe')

   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys('vasya@mail.com')
   sleep(1)

   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys("12345")
   sleep(1)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   sleep(1)

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"