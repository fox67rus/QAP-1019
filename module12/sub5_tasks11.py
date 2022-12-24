# словари

# title = input("Введите название книги: ")
# author = input("Введите автора: ")
# year = input("Введите год выпуска: ")
book = {}

title = "1984"
author = "Джордж Оруэлл"
year = "1949"

book['title'] = title.strip()
book['author'] = author.strip()
book['year'] = int(year.strip())

print(book)
