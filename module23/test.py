# WorkShop по работе с локаторами и прерываниями
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker


class TestLoginStellarBurgers:

    def setup(self):
        self.user = 'kuzya@testmail.ru'
        self.password = '123456'

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def close(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(self.user)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        # проверяем, что после авторизации появилась кнопка Оформить заказ
        assert WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))


    def test_login_by_button_in_form(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[contains(text(),'Войти в аккаунт')]"))).click()
        self.login()

    def test_login_from_cabinet(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.XPATH,
            "//p[contains(text(),'Личный Кабинет')]")))).click()
        self.login()

    def test_registration(self):
        fake_name = Faker().name()
        fake_email = Faker().email()
        fake_password = Faker().password()
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//a[@href='/register']"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//label[text() = 'Имя']/following-sibling::input"))).send_keys(fake_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//label[text() = 'Email']/following-sibling::input"))).send_keys(fake_email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='password']"))).send_keys(fake_password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]"))).click()


        # sleep(5) # плохой способ сделать задержку, чтобы увидеть заполнение данных

    def teardown(self):
        self.close()
