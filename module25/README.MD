## 25.2. Виды локаторов в Selenium

### Поиск по CSS селектору
driver.find_element(By.CSS_SELECTOR, "element_css_selector")
- input — селектор находит все элементы с тегом инпут.
- #unique-id — селектор находит все элементы с id = unique-id.
- .some-class — селектор находит все элементы с классом some-class.
- input[type=’submit’] — селектор находит все элементы с тегом input и атрибутом type, равным submit.
- div > input — селектор находит все элементы с тегом input, которые находятся непосредственно внутри элемента с тегом div. 
- div input — селектор находит все элементы с тегом input, которые находятся внутри элемента с тегом div на любом уровне вложенности.

### Поиск по XPath
element = driver.find_element(By.XPATH, "element_xpath")

**//tag-name**
Поиск из любого места документа (веб-страницы). В примере выше запись //input означает поиск тега input в любом месте документа. Допускается использование вложенности, то есть //form//input — поиск тега input внутри формы на любом уровне.

**/tag-name**
То же, что в предыдущем пункте, но поиск осуществляется на один уровень вниз, то есть //form/input ищет форму в любом месте документа и input строго на следующем уровне вложенности.
Если поиск осуществляется по /form/input, то поиск тега form будет выполнен от начала документа (внутри непосредственно тега body).

**[@id="name"]**
Для поиска по атрибутам элемента достаточно открыть квадратные скобки и указать имя атрибута с префиксом “@”. В примере выше //input[@id="name"] мы ищем тег input с атрибутом id равным name.

**(@class=”...”)**
Аналогично происходит поиск по классу (@class=”...”), имени (@name=”...”) и любым другим, в том числе пользовательским, атрибутам.
Например, если у тега есть атрибут custom-data-id, то XPath позволяет найти и по нему (@custom-data-id=”...”).
Для сложных случаев допускается использование логических операторов И и ИЛИ. Например, //input[@id=”1” or @class=”my-class”] надёт элементы с id равным единице или с классом my-class. Оператор И в XPath пишется через and.

**//input[text()=”Опция 1”]**
XPath позволяет искать элемент по тексту внутри него. Отдельного атрибута для этой опции нет, но поиск происходит аналогично атрибутам.
Чтобы выполнить поиск внутри элемента по тексту, необходимо написать условие text()=”...”. Например, выражение //input[text()=”Опция 1”] будет искать все теги input внутри которых текст будет в точности равен “Опция 1”.
Для поиска по части текста необходимо использовать оператор contains. Так выражение //input[contains(text(), ”Опция 1”)] найдёт все инпуты, внутри которых текст будет содержать подстроку “Опция 1”.

**ancestor::tag-name**
Чтобы найти предка элемента, необходимо добавить команду ancestor::tag-name в выражение XPath. Например, выражение //input[type=”button”]/ancestor::form найдёт все формы, в которые вложен элемент input с типом button.

## 25.4. Ожидания в Selenium
### Явные ожидания
WebDriverWait — это специальный класс WebDriver, который помогает нам в реализации явных ожиданий. 

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
# Может читаться как «ожидаем в течение 10 секунд драйвером driver появления элемента с локатором id=myDynamicElement».
```

Доступные методы для работы с ожиданиями:
1. title_is — ожидаем, что заголовок окна равен указанной строке (заголовок окна браузера, а не тег h1-h6 в структуре документа). 
2. title_contains — ожидание, что заголовок окна содержит определённую строку текста. 
3. presence_of_element_located — ВНИМАТЕЛЬНО! Ожидание присутствия элемента в структуре документа. 
4. visibility_of_element_located — ВНИМАТЕЛЬНО! Ожидание видимости элемента на экране. 
5. visibility_of — ожидание видимости элемента WebElement (например, элемент, который ранее найден с помощью метода driver.find_elements_by_css_selector). 
6. presence_of_all_elements_located — ожидание присутствия в документе всех элементов, найденных с помощью указанного локатора. 
7. text_to_be_present_in_element — ожидание определённого текста внутри указанного элемента. 
8. text_to_be_present_in_element_value — ожидание определённого текста внутри атрибута value элемента. 
9. frame_to_be_available_and_switch_to_it — ожидание появления iframe на странице и переключение на него. 
10. invisibility_of_element_located — ожидание невидимости элемента, найденного по указанному локатору. 
11. element_to_be_clickable — ожидание активности элемента, являющегося экземпляром класса WebElement. 
12. element_to_be_selected — ожидание, что элемент в выпадающем списке выбран. 
13. element_located_to_be_selected — то же, что и предыдущая функция, но указывать элемент нужно через функции поиска (find_element_by_id, find_element_by_name и так далее). 
14. element_selection_state_to_be — ожидание, что элемент выпадающего списка имеет определённое состояние. 
15. element_located_selection_state_to_be — то же, что и предыдущая функция, но требуется поиск элемента через функции поиска (find_element_by_id, find_element_by_name и так далее). 
16. alert_is_present — ожидания всплывающего окна на странице браузера.

### Пользовательские ожидания
Функция, которая принимает на вход WebElement и ожидает, что у него появится определенный CSS-класс.
```python
class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False
```
Итак, мы объявили класс element_has_css_class и написали внутри него конструктор, который принимает 2 аргумента:

Локатор, по которому мы будем искать элемент.
Название класса, которое ожидаем найти.
Для того чтобы функция until могла работать с нашим классом, нам необходимо написать функцию __call__, логика которой 
очень проста: мы находим элемент на странице по указанному локатору, получаем из этого элемента атрибут class и смотрим, 
есть ли среди классов элемента искомый. Если да, то возвращаем сам элемент, а иначе возвращаем False.
Вызов в коде:
```python
wait = WebDriverWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, 'checklistItem'), "greenChecklistItem"))
```

### Неявные ожидания
```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```
Такое ожидание проигрывает в функциональности, так как реализует, по сути, только одну функцию: поиск элемента на странице. 
Оно также проигрывает и в гибкости настройки, так как время ожидания мы можем задавать только в момент, когда настраиваем 
WebDriver для работы со страницами. В случае с явными ожиданиями мы можем указать разное время ожидания для разных страниц, 
используя разные экземпляры класса WebDriverWait, даже в пределах одной страницы мы можем задать разные интервалы ожиданий для разных типов элементов.


