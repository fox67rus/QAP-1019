# run test
# python -m pytest -v --driver Chrome --driver-path ..\drivers\chromedriver.exe

from module26.pages.auth_page import AuthPage
import time

def test_auth_page_invalid_data(driver):
    page = AuthPage(driver)
    page.enter_email("email@gmail.com")
    page.enter_pass("pass0")
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() != '/all_pets', 'Login error'

    time.sleep(3)

def test_auth_page_valid_data(driver):
    page = AuthPage(driver)
    page.enter_email("test@qiott.com")
    page.enter_pass("Qwerty_123")
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() == '/all_pets', 'Login error'

    time.sleep(3)
