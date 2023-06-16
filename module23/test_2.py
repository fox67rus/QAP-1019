from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_python_org():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org/")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    sleep(5)
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

    sleep(5)
    assert "No result found." not in driver.page_source
    driver.close()


def test_PF_login():
    driver = webdriver.Chrome()
    driver.get("https://petfriends.skillfactory.ru/login")
    assert "PetFriends" in driver.title

    login = driver.find_element(By.NAME, "email")
    login.clear()
    sleep(2)
    login.send_keys("test@qiott.com")

    sleep(5)

    password = driver.find_element(By.NAME, "pass")
    password.clear()
    sleep(2)
    password.send_keys("Qwerty_123")
    sleep(5)
    password.send_keys(Keys.RETURN)
    # assert "0 проектов по запросу" not in driver.page_source
    sleep(5)
    driver.close()


def test_tutu():
    driver = webdriver.Chrome()
    driver.get("https://www.tutu.ru/")
    assert "Tutu" in driver.title

    driver.find_element(By.XPATH, "//div[contains(text(),'Электрички')]").click()
    sleep(1)
    assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "st1")))
    driver.find_element(By.NAME, "st1").send_keys("гагарин")
    sleep(2)
    driver.find_element(By.NAME, "st2").send_keys("вязьма")
    sleep(2)
    # driver.find_element(By.XPATH, "//input[@placeholder='Дата']").clear()
    # driver.find_element(By.XPATH, "//input[@placeholder='Дата']").send_keys("16.06.2023, пт")

    # driver.find_element(By.XPATH, "//button[@data-ti='date_arrow_reduce']").click()
    # driver.find_element(By.XPATH, "//button[@data-ti='date_arrow_increase']").click()
    sleep(2)
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-handler='today']"))).click()
    # sleep(2)
    driver.find_element(By.TAG_NAME, "button").click()
    sleep(5)
    driver.quit()
