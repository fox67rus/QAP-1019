# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
# читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
# В файле ожидается смешанный текст на двух языках — русском и английском.


# filename = input("Введите имя файла, например - en_rus.txt:\n")
filename = 'en_rus.txt'
all_words = []
marks = ['!', '(', ')', '-', ';', '?', ':', '\n', ',', '.', '«', '»']

with open(filename, encoding='utf-8') as myFile:
    for line in myFile:
        new_line = line.split(' ')  # list

        for word in new_line:  # str
            word = word.lower()
            if not word.isalnum():
                for mark in marks:
                    word = word.replace(mark, '')
            # print(f'{word=} {type(word)=}')
        if word:
            all_words.append(word)

        # all_words += list(map(str.lower, word))

    print(all_words)
    # all_words.append(line.replace('\n', '').split(' '))
