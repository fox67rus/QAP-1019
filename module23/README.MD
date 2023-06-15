# Модуль 23

- Локатор элемента по ID — document.getElementById("id")
- Локатор элемента по атрибуту name — document.getElementsByName("name")
- Локатор по названию класса — document.getElementsByClassName("className")
- CSS-локатор — document.querySelectorAll("css") или $$("css")
  - точка (.) ставится перед именем класса 
  - решетка (#) — перед идентификатором 
  - пробел — перед спуском «вниз»
  - $$('div[dev-id="01"]') - обращение к произвольному атрибуту
  - если в имени класса есть служебный символ, то ставить \\ ($$(".\\.col-sm-4.left"))
### Шаги получения CSS-локатора для выбранного элемента:
Выбрать элемент.
Выбрать в контекстном меню Inspect.
В подсвеченной строке кода вызвать контекстное меню.
В контекстном меню навести на пункт Copy.
В выпадающем меню выбрать Copy JS path.
Перейти на вкладку Console.
Выполнить вставку (Ctrl+V) или вызвать контекстное меню и выбрать «Вставить».

### Шаги получения XPath для выбранного элемента:
Выбрать элемент.
Выбрать в контекстном меню Inspect.
В подсвеченной строке кода вызвать контекстное меню.
В контекстном меню навести на пункт Copy.
В выпадающем меню выбрать Copy XPath.

- XPath-локатор — $x('//x[@path]')
  - звёздочка(*) означает произвольный тег $x('//*[@id="name"]')
  - квадратные скобки — [ ] — обращение к атрибутам тега 
  - собака @ бегает и виляет хвостом перед каждым атрибутом $x('//input[@id="name"]')
  - В XPath индексация начинается с 1, а не с 0
  - В XPath значение атрибута класс копируется «как есть» — с пробелом или с точкой
  - если указать только атрибут без значения, то можно узнать, используется ли вообще атрибут на странице, и если да, то сколько раз $x('//*[@id]')
Общая формула написания относительного XPath — двойной слеш, тег, квадратные скобки, собачка, атрибут, значение. 
«Спуск» по иерархии DOM-дерева осуществляется при помощи косой черты.
//tagname[@attribute='value']
Итоговый локатор: //div[@class=".col-sm-4 left"]/h2.

## XPATHs tricks
### Трюк № 1. Получение значения атрибутов
Для получения значения атрибута ввести в консоль $x('//a[@data-panel="m-nav-panel-products"]/@href'). 
Значение видно в раскрывающемся списке, в пункте nodeValue

Для получения текста внутри тега использовать специальный атрибут /text()
$x('//a[@data-panel="m-nav-panel-products"]/text()')

### Трюк № 2. Поиск по содержимому в атрибутах и тексте
Используется служебный указатель contains, который получает два параметра: 
в каком атрибуте искать и что искать (после запятой). 

- $x('//a[contains(text(), "Products")]') - Находит все теги ссылок, внутри которых есть текст "Products". 
- $x('//div[contains(@class, "m-nav-panel")]') - Находит все div у которых в имени класса есть строчка "m-nav-panel". 
- $x('//img[contains(@src, ".png")]') - Находит все png-картинки.


### Трюк № 3. Поиск по нескольким атрибутам
Используется слово and, значок атрибута @ и значение атрибута. При помощи слова or мы можем найти все элементы, 
 у которых присутствует хотя бы один атрибут из указанных.
$x('//div[@class="lb-xb-grid-wrap" and @style="margin-bottom:30px;"]') 
$x('//div[@class="lb-xb-grid-wrap" or @style="margin-bottom:30px;"]')

### Трюк № 4. Вниз и вверх по DOM
Сначала укажем div , который содержит карту: $x('//div[@data-lb-comp="gi-map"]'). Затем мы можем указать последовательно всех предков до желаемой ссылки, и также можем сократить путь ещё раз, использовав двойной прямой слеш. Тем самым мы указываем, что тег после двойного следует искать в любом месте внутри тега-родителя с атрибутом data-lb-comp="gi-map".

$x('//div[@data-lb-comp="gi-map"]//a') — такой XPath указывает на 5 элементов.

Но внутри ссылки Learn More есть еще тег <i>. Если мы укажем его, то получим локатор, указывающий на 
один элемент://div[@data-lb-comp="gi-map"]//a/i. Но ведь мы изначально хотели получить локатор для ссылки. 
Теперь мы можем сделать это, просто вернувшись наверх по DOM-дереву при помощи команды .. (две точки подряд):  $x('//div[@data-lb-comp="gi-map"]//a/i/..').

### Практика
- document.getElementById('__BVID__10')
- document.getElementById("inline-form-input-species")
- document.getElementsByClassName("tail container-fluid")
- $x('//div[@class="lb-tabs lb-tabs-minimal-text-dark-bg" and @style="background-color:#232f3e;" and @data-lb-comp="tabs" and @data-lb-comp-registered="true"]')
- $$('.instagram.icon')
- $x('//a[contains(text(), "О нас")]')
- $x('//a[contains(@aria-label, "Go to page 1")]')
- $x('//button[contains(text(), "без дома") and @class="btn btn btn-secondary wait"]')

## Дополнительно 
### Статьи по CSS:
1. [Документация Mozilla](https://developer.mozilla.org/ru/docs/Web/CSS/CSS_%D0%A1%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D1%8B); 
2. [Как использовать CSS для идентификации элементов](https://www.softwaretestinghelp.com/css-selector-selenium-locator-selenium-tutorial-6/); 
3. [Краткий справочник](https://html5css.ru/cssref/css_selectors.php). 

### Статьи по Xpath:
1. [Документация Mozilla](https://developer.mozilla.org/en-US/docs/Web/XPath); 
2. [Учебник по XPath](https://msiter.ru/tutorials/xpath); 
3. [Руководство по написанию XPath](https://www.guru99.com/xpath-selenium.html#1); 
4. [Шаблоны XPath](https://devhints.io/xpath). 

### Применение в автоматизации:
1. [Типы локаторов](https://comaqa.gitbook.io/selenium-webdriver-lectures/selenium-webdriver.-vvedenie/tipy-lokatorov); 
2. [Вебинар на Хабре: Как создавать локаторы для Selenium WebDriver](https://habr.com/ru/post/144063/); 
3. [Локаторы. CSS, XPATH, JQUERY](https://comaqa.gitbook.io/selenium-webdriver-lectures/selenium-webdriver.-slozhnye-voprosy./lokatory.-css-xpath-jquery.); 
4. [Selenium: знакомимся с локаторами и выбираем правильный](https://automated-testing.info/t/selenium-znakomimsya-s-lokatorami-i-vybiraem-pravilnyj/2268).