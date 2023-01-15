# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
# читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
# В файле ожидается смешанный текст на двух языках — русском и английском.

def is_english(text:str) -> bool:
    """ Определяет на английском языке слово или нет """
    pass

def delete_special_char(text:str) -> str:
    """ Удаляем все переносы и спецсимволы из текста text и возвращает текст без спецсимволов"""
    marks = ['!', '(', ')', '-', ';', '?', ':', '\n', ',', '.', '«', '»']
    for mark in marks:
        text = text.replace(mark, '')
    return text

def prepare_text_from_file(file_):
    """ Обрабатывает текст из файла """
    pass


# filename = input("Введите имя файла, например - en_rus.txt:\n")
filename = 'en_rus.txt'
all_words = []


with open(filename, encoding='utf-8') as file:
    for line in file:
        line = line.split(' ')  # list

        for word in line:  # str
            word = word.lower()
            if not word.isalnum():
                word = delete_special_char(word)

        # пропускаем пустые слова
        if word:
            all_words.append(word)

    print(all_words)
