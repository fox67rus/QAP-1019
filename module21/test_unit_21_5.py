import sys

import pytest

@pytest.mark.skip(reason='Баг в продукте - <ссылка>')
def test_one():
    pass

@pytest.mark.skipif(sys.version_info < (3, 9), reason='Тест требует python версии 3.9 или выше')
def test_python39_and_greater():
    pass

# высокая вероятность, что тест упадет
@pytest.mark.xfail
def test_flaky():
    assert 1 == 2

# На платформе Windows ожидаем, что тест будет падать
@pytest.mark.xfail(sys.platform == 'win32', reason='ошибка в системной библиотеке')
def test_not_for_windows():
    pass

# собственные метки
@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
    pass

@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
    pass

@pytest.mark.api
@pytest.mark.event
def test_event_api():
    pass

@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
    pass

# pytest -v -s -m "api or event"

