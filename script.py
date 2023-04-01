import pytest


@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)  # название фикстуры
    print(request.scope)  # её область видимости
    print(request.function.__name__)  # название теста
    print(request.cls)  # название класса
    print(request.module.__name__)  # Название модуля
    print(request.fspath)  # путь до файлика, из которого запущен наш тест
    if request.cls:  # Последней строкой выводится информация о том, запущен ли наш тест из класса или нет.
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)


class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)

