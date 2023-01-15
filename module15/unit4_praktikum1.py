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
    """ Удаляет все переносы и спецсимволы из текста text и возвращает текст без спецсимволов"""
    marks = ['!', '(', ')', '-', ';', '?', ':', '\n', ',', '.', '«', '»']
    for mark in marks:
        text = text.replace(mark, '')
    return text


def count_rep_words(words: list, min_number_char: int = 3) -> dict:
    """
    Считает количество повторений слов в списке, если слово длиннее определенного количество букв.
    :param words: Список слов
    :param min_number_char: минимальное количество символов в слове
    :return: словарь вида 'слово': количество повторений в списке
    """
    count = {}  # для подсчета слов и их количества
    for word in words:
        if len(word) > min_number_char:
            if word in count:  # если слово уже встречалось, то увеличиваем его количество на 1
                count[word] += 1
            else:
                count[word] = 1
    return count


def search_max_value(input_dict: dict) -> dict:
    """
    Поиск ключей (слов) наиболее часто встречающихся в словаре
    :param input_dict:
    :return: словарь с найденным словом или словами, если несколько слов имеют одинаковое количество повторений
    """
    if input_dict:
        max_frequent_value = max(input_dict.values())
        out_dict = {k: v for k, v in input_dict.items() if v == max_frequent_value}
        count_word = len(out_dict)
        if count_word > 1:
            print(f'Найдено несколько слов ({count_word} шт.) удовлетворяющим условиям поиска:')
            for word, cnt in out_dict.items():
                print(f'Слово - "{word}", количество повторений в тексте - {cnt}')

        return out_dict
    else:
        print('Не найдено слов, с выбранными параметрами. Проверьте ограничение количества букв')


def is_english(text: str) -> bool:
    """ Возвращает True если слово на английском языке """
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def search_max_length(input_dict: dict) -> list:
    """
    Поиск самого длинного слова на английском
    :param input_dict:
    :return: возвращает список кортежей вида ('слово', количество символов) со словом или словами, если найдено
             несколько слов с одинаковым количеством символов
    """
    if input_dict:
        words_list = list(input_dict)
        eng_word_list = []
        for word in words_list:
            if is_english(word):
                eng_word_list.append(word)

        print(f'\nСписок ({len(eng_word_list)}) английских слов - {eng_word_list})')

        max_length = 0
        out_list = []
        for word in eng_word_list:
            if len(word) > max_length:
                out_list = []
                max_length = len(word)
                out_list.append((word, max_length))
            elif len(word) == max_length:
                out_list.append((word, max_length))

        count_word = len(out_list)
        if count_word > 1:
            print(f'Найдено несколько слов ({count_word} шт.) с одинаковым количеством символов:')
            for word, length in out_list:
                print(f'Слово - "{word}", количество символов - {length}')
        else:
            print(f'Самое длинное слово на английском - {out_list[0][0]}. В нём {out_list[0][1]} букв')
        return out_list

    pass


def main(textfile: str):
    all_words = prepare_text_from_file(textfile)
    word_with_rep = count_rep_words(all_words)
    search_max_value(word_with_rep)
    search_max_length(word_with_rep)


if __name__ == '__main__':
    # filename = input("Введите имя файла, например - en_rus.txt:\n")
    # char_limit = input("Минимальное количество символов в слове: \n")
    filename = 'en_rus.txt'
    main(filename)
