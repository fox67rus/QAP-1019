import pytest
from pages.auth_page import AuthPage

def test_auth(web_browser):
    page = AuthPage(web_browser)
    page.email.send_keys('vasya@mail.com')
    page.password.send_keys('12345')
    page.bth.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/login'
