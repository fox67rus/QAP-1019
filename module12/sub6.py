L = ['a', 'b', 'c']
print(id(L))
L.append('d')
print(id(L))

a = 5
b = 3+2
print(f"{id(a)= }, {id(b)= }, {id(a) - id(b) = }")

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)
print(list_1 == list_2)
print(list_1 == list_3)
print(list_1 is list_2)
print(list_1 is list_3)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
shopping_center[-1].append("Uniqlo")
print(shopping_center)
# ('Галерея', 'Санкт-Петербург', 'Лиговский пр., 30', ['H&M', 'Zara', 'Uniqlo'])