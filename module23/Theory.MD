# Модуль 23

- Локатор элемента по ID — document.getElementById("id")
- Локатор элемента по атрибуту name — document.getElementsByName("name")
- Локатор по названию класса — document.getElementsByClassName("className")
- CSS-локатор — document.querySelectorAll("css") или $$("css")
  - точка (.) ставится перед именем класса 
  - решетка (#) — перед идентификатором 
  - пробел — перед спуском «вниз»

- XPath-локатор — $x('//x[@path]')
  - звёздочка(*) означает произвольный тег 
  - квадратные скобки — [ ] — обращение к атрибутам тега 
  - собака @ бегает и виляет хвостом перед каждым атрибутом 

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