from datetime import datetime
from module21.petFriendsTesting.tests.test_pet_friends import pf, valid_password, valid_email
import pytest


# должно быть несколько групп функциональных тестов, которые описаны в ini файле. Есть тесты, помеченные как xfail, skip

@pytest.fixture(autouse=True)
def get_key():
    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    return auth_key

@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")

@pytest.fixture
def log(request):
    start_time = datetime.now()
    yield
    end_time = datetime.now()

    print()  # название теста

    with open('log.txt', 'a', encoding="utf-8") as f:
        f.write(f'Тест {request.function.__name__}. Начало в {start_time}, окончание в {end_time} , тест шёл {end_time - start_time} \n')


