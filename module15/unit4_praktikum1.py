# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
# читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
# В файле ожидается смешанный текст на двух языках — русском и английском.

def prepare_text_from_file(file_, info: bool = False) -> list:
    """
    Обрабатывает текст из файла.
    :param file_: Файл с текстом от пользователя
    :param info: если указан истинный, то выводить статистику по полученному тексту: количество слов и уникальных слов
    :return: возвращает список не пустых слов в нижнем регистре, без спецсимволов
    """
    words_list = []
    with open(file_, encoding='utf-8') as file:  # добавить обработку FileNotFoundError
        for line in file:
            line = line.split(' ')  # list

            for word in line:  # str
                word = word.lower()
                if not word.isalnum():
                    word = delete_special_char(word)

                # добавляем в список, пропуская пустые слова
                if word:
                    words_list.append(word)
        if info:
            print(f'Сформирован список всех слов из полученного текста:\n{words_list}')
            print(f'Всего слов в тексте - {len(words_list)}, в том числе уникальных - {len(list(set(words_list)))}\n')

        return words_list


def delete_special_char(text: str) -> str:
    """ Удаляем все переносы и спецсимволы из текста text и возвращает текст без спецсимволов"""
    marks = ['!', '(', ')', '-', ';', '?', ':', '\n', ',', '.', '«', '»']
    for mark in marks:
        text = text.replace(mark, '')
    return text


def count_words(words: list) -> dict:
    """ Считает количество повторений слов в списке. На выходе словарь вида 'слово': количество повторений в списке """
    count = {}  # для подсчета слов и их количества
    for word in words:
        if word in count:  # если слово уже встречалось, то увеличиваем его количество на 1
            count[word] += 1
        else:
            count[word] = 1

    # for word, cnt in count.items():
    #     print(f'Слово "{word}" встречается {cnt} раз')

    return count


def is_english(text: str) -> bool:
    """ Определяет на английском языке слово или нет """
    pass


if __name__ == '__main__':
    # filename = input("Введите имя файла, например - en_rus.txt:\n")
    filename = 'en_rus.txt'
    all_words = prepare_text_from_file(filename, True)
    print(count_words(all_words))
