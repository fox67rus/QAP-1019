from cat import Cat

Baron = Cat("Барон", 'мальчик', 2)
Sam = Cat("Сэм", 'мальчик', 2)

print(f'Кличка: {Baron.get_name()}, Возраст: {Baron.get_age()}, Пол: {Baron.get_gender()}')
print(f'Кличка: {Sam.get_name()}, Возраст: {Sam.get_age()}, Пол: {Sam.get_gender()}')