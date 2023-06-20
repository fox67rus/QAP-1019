# Более сложный сценарий для проекта PetFriends.
# Авторизация клиента, залогиниться и получить скриншот стартовой страницы.
# run test:
# cd module24
# python -m pytest -v --driver Chrome --driver-path drivers\chromedriver.exe test_selenium_petfriends.py

import time

from selenium.webdriver.common.by import By

def test_petfriends(selenium):
    selenium.get("https://petfriends.skillfactory.ru/")
    time.sleep(2)

    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()
    time.sleep(2)

    btn_exist_acc = selenium.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()
    time.sleep(2)

    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("test@qiott.com")
    time.sleep(1)

    field_password = selenium.find_element(By.ID, "pass")
    field_password.clear()
    field_password.send_keys("Qwerty_123")
    time.sleep(1)

    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()
    time.sleep(2)

    if selenium.current_url == "https://petfriends.skillfactory.ru/all_pets":
        # selenium.find_element(By.LI, "Мои питомцы").click()
        selenium.save_screenshot("result_petfriends.png")
        time.sleep(2)
    else:
        raise Exception("login error")










