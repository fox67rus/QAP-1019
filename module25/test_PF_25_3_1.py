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
    sleep(1)

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"


    yield

    pytest.driver.quit()

def test_my_pets_page():
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
    sleep(1)
    assert pytest.driver.current_url == "https://petfriends.skillfactory.ru/my_pets"

    user_info = pytest.driver.find_element(By.CSS_SELECTOR,"div.task3.fill > div")
    # print(f'{len(user_info.text)=}')
    # print(f'{user_info.text=}')
    expected_pets = int(user_info.text.split('\n')[1][-1])
    # print(f'{expected_pets=}')

    actual_pets=pytest.driver.find_elements(By.XPATH, '//tbody/tr')
    assert expected_pets == len(actual_pets), "Присутствуют не все питомцы" # задание 1
    # print(f'{len(actual_pets)=}')

    pets_photos = pytest.driver.find_elements(By.CSS_SELECTOR, 'th > img')
    print(len(pets_photos))
    pets_with_photos = 0
    for img in range(len(pets_photos)):
        if pets_photos[img].get_attribute('src') != '':
            pets_with_photos += 1
    assert pets_with_photos > expected_pets / 2, "Больше половины питомцев без фото" # задание 2


    pets_names = []
    pets_info_dict = {}
    for i in range(len(actual_pets)):
        # print(actual_pets[i].text[:-2])
        pet_info = actual_pets[i].text[:-2].split(' ')
        assert len(pet_info) == 3, "не у всех питомцев есть имя, возраст и порода"  # задание 3
        pets_names.append(pet_info[0])
        # print(f'{pet_info=}')
        pets_info_dict[i + 1] = pet_info

        # assert pet_info[0] != ''
        # assert pet_info[1] != ''
        # assert pet_info[2] != ''


    duplicate_names = []
    # print(f'{pets_names=}')
    no_double_names_flag = True
    for item in pets_names:
        if item not in duplicate_names:
            duplicate_names.append(item)
        else:
            no_double_names_flag = False
    assert no_double_names_flag, "не у всех питомцев разные имена" # задание 4

    print(f'{pets_info_dict=}')
    # has_dupes = len(pets_info_dict) != len(set(pets_info_dict.values()))
    print(f'{pets_info_dict.values()=}')
    print({v: [k for k in pets_info_dict if pets_info_dict[k] == v] for v in set(pets_info_dict.values())})
    # values = list(pets_info_dict.values())
    # if len(values) == len(set(values)):
    #     print("no duplicates")
    # else:
    #     print("duplicates")









    # assert images[i].get_attribute('src') != ''
    # assert descriptions[i].text != ''
    # assert ', ' in descriptions[i]
    # parts = descriptions[i].text.split(', ')
    # assert len(parts[0]) > 0
    # assert len(parts[1]) > 0

    # actual_pets =


    # images = pytest.driver.find_elements(By.CSS_SELECTOR, 'tbody > tr > th > img')
    # descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

