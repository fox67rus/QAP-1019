s = "Hello!"
s1 = 'hello' # используя апострофы
s2 = "hola" # используя кавычки
s3 = '''Привет!
        Хорошего дня!''' # используя тройные "апострофы" или тройные кавычки

print(s[::2])
print(len(s))

print(s.isdigit()) # строка состоит из цифр?
print(s.isalpha()) # строка состоит из букв?
print(s.isalnum()) # строка состоит из цифр и букв?

print(s.upper())
# HELLO!

print(s.lower())
# hello!

print(s)
# Hello! - исходная строка не изменяется

path = '/home/user/documents/file.txt'
print(path.split('/')) # разделитель можно указать в качестве аргумента
# ['', 'home', 'user', 'documents', 'file.txt']

colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue

age = 25

my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d

print(my_age)
# I'm 25 years old

pi = 31.4159265
print ("%.4e" % (pi))

day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2