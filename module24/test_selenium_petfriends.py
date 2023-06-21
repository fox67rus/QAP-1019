# Более сложный сценарий для проекта PetFriends.
# Авторизация клиента, залогиниться и получить скриншот стартовой страницы.
# run test:
# cd module24
# python -m pytest -v --driver Chrome --driver-path drivers\chromedriver.exe test_selenium_petfriends.py

import time

from selenium.webdriver.common.by import By

def test_petfriends(selenium):
    selenium.get("https://petfriends.skillfactory.ru/")
    time.sleep(1)

    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()
    time.sleep(1)

    btn_exist_acc = selenium.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()
    time.sleep(1)

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
    time.sleep(1)

    if selenium.current_url == "https://petfriends.skillfactory.ru/all_pets":
        # selenium.find_element(By.LI, "Мои питомцы").click()
        selenium.save_screenshot("result_petfriends.png")
        time.sleep(2)
    else:
        raise Exception("login error")


def test_petfriends_trick(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("test@qiott.com")

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("Qwerty_123")
    time.sleep(1)

    # click submit button
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"










