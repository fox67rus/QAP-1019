# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
# читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
# В файле ожидается смешанный текст на двух языках — русском и английском.

def prepare_text_from_file(file_) -> list:
    """ Обрабатывает текст из файла """
    words_list = []
    with open(file_, encoding='utf-8') as file:
        for line in file:
            line = line.split(' ')  # list

            for word in line:  # str
                word = word.lower()
                if not word.isalnum():
                    word = delete_special_char(word)

            # пропускаем пустые слова
            if word:
                words_list.append(word)
        return words_list


def delete_special_char(text: str) -> str:
    """ Удаляем все переносы и спецсимволы из текста text и возвращает текст без спецсимволов"""
    marks = ['!', '(', ')', '-', ';', '?', ':', '\n', ',', '.', '«', '»']
    for mark in marks:
        text = text.replace(mark, '')
    return text


def count_words(words: list) -> dict:
    """ Считает количество повторений слов в списке. На выходе словарь вида 'слово': количество повторений """
    pass


def is_english(text: str) -> bool:
    """ Определяет на английском языке слово или нет """
    pass


if __name__ == '__main__':
    # filename = input("Введите имя файла, например - en_rus.txt:\n")
    filename = 'en_rus.txt'
    all_words = prepare_text_from_file(filename)
    print(all_words)
