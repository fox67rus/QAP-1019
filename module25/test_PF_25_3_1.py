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

    # Вводим пароль
    pytest.driver.find_element(By.ID, "pass").send_keys("Qwerty_123")

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"

    yield

    pytest.driver.quit()


def test_my_pets_page():
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
    sleep(1)
    assert pytest.driver.current_url == "https://petfriends.skillfactory.ru/my_pets"

    user_info = pytest.driver.find_element(By.CSS_SELECTOR, "div.task3.fill > div")
    # print(f'{len(user_info.text)=}')
    # print(f'{user_info.text=}')
    expected_pets = int(user_info.text.split('\n')[1][-1])
    # print(f'{expected_pets=}')

    actual_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr')
    # Проверяем что количество строк таблицы соответствует количеству питомцев в блоке статистики пользователя
    assert expected_pets == len(actual_pets), "Присутствуют не все питомцы"  # задание 1

    # print(f'{actual_pets=}')

    pets_photos = pytest.driver.find_elements(By.CSS_SELECTOR, 'th > img')
    # print(f'{len(pets_photos)=}')
    pets_with_photos = 0
    for img in range(len(pets_photos)):
        if pets_photos[img].get_attribute('src') != '':
            pets_with_photos += 1
    assert pets_with_photos >= expected_pets / 2, "Больше половины питомцев без фото"  # задание 2

    pets_names = []
    pets_list = []
    for i in range(len(actual_pets)):
        pet_info = actual_pets[i].text[:-2].split('\n')
        assert len(pet_info[0].split()) == 3, "не у всех питомцев есть имя, возраст и порода"  # задание 3
        # print(f'{pet_info=}')
        pets_names.append(pet_info[0])
        pets_list.append(" ".join(pet_info))
        # print(f'{pet_info=}')
        # print(f'{pets_names=}')
    print(f'\n{pets_list=}')

    pet_names = [elem.split()[0] for elem in pets_list]
    # print(f'\n{pet_names=}')
    assert len(pet_names) == len(set(pet_names)), 'не у всех питомцев разные имена.'  # задание 4
    assert len(pets_list) == len(set(pets_list)), 'Есть повторяющиеся питомцы'  # задание 5
