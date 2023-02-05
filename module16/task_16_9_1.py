# Создайте класс одной из геометрических фигур (например, прямоугольника), где в конструкторе задаются атрибуты:
# начальные координаты x, y, width и height (или другие в зависимости от выбранной фигуры).
#
# Создайте метод, который возвращает атрибуты прямоугольника как строку
# (постарайтесь применить магический метод __str__).
#
# Для объекта прямоугольника со значениями атрибута x = 5, y = 10, width = 50, height = 100
# метод должен вернуть строку Rectangle : 5, 10, 50, 100.

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'


rectangle = Rectangle(5, 10, 50, 100)
print(rectangle)
