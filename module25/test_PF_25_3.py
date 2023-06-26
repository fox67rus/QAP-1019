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


def test_show_all_pets():
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

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   ################################################################
   # print(f'{len(images)=}')
   # print(f'{len(names)=}')
   # print(f'{len(descriptions)=}')
   # with open("file.txt", 'a') as f:
   #    f.write('names:' + '\n')
   #    for i, el in enumerate(names):
   #       f.write(f'{i+1 } {el.text}'+'\n')
   #
   #    f.write('images:' + '\n')
   #    for i, el in enumerate(images):
   #       f.write(f'{i + 1} {el.get_attribute("src")[:25]}' + '\n')
   #
   #    f.write('descriptions:' + '\n')
   #    for i, el in enumerate(descriptions):
   #       f.write(f'{i + 1} {el.text}' + '\n')
   ################################################################


   for i in range(len(names)):
      assert names[i].text != ''
      assert images[i].get_attribute('src') != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(', ')
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

def test_my_pets():
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