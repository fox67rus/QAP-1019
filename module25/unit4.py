from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.wildberries.ru/")

# Реализация явных ожиданий
element = WebDriverWait(driver, 10).until( # передаем драйвер и время максимального ожидания в секундах
    EC.presence_of_element_located((By.ID, "searchInput")) # условие, выполнение которого ожидается в предыдущей строке
)                                                          # ждём появление элемента с указанным ID
driver.quit()