# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']

# с помощью метода append() мы добавляем ещё один элемент в список
letters.append('e')

print(letters)
# ['a', 'b', 'c', 'd', 'e']

letters.append('f') # добавляем ещё одну букву
letters.append('g') # и ещё одну
print(letters[len(letters)-1])

print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters.pop() # вызов метода без аргументов удаляет последний элемент списка

print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f']
# был удалён последний элемент

letters.pop(0) # или можно удалить элемент по его индексу

print(letters)
# ['b', 'c', 'd', 'e', 'f']
# был удалён нулевой элемент

letters.pop(3) # и не обязательно удалять из начала или конца списка

print(letters)
# ['b', 'c', 'd', 'f']
# был удалён элемент с индексом 3


# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6]

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
#[3, 4, 6, 7]

L = ['3.3', '4.4', '5.5', '6.6']
print (list (map (float, L)))


string = "1 1 2 3 5 8 13 21 34 55"

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел

print(sum(list_of_numbers[::1])) # sum() вычисляет сумму элементов списка

# словари
person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}


abits = [abit1, abit2, abit3]

print(abits)

# множества
L = [1,1,2,3,2]
b = set(L)
print(b)
# {1,2,3}
b_list = list(b)
print(b_list)
# [1,2,3]
print(list(set(L)))

abons = {"Иванов", "Петров", "Васильев", "Антонов"}
debtors = {"Петров", "Антонов"}
non_debtors = abons.difference(debtors)
print(non_debtors)
# {'Васильев', 'Иванов'}
