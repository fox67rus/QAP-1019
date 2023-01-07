# Задание 13.8.18. Реализуйте программу, которая сжимает последовательность символов
text = "aaabbccccdaa"
print(text)
new_text = ''
count = 0
for i, char in enumerate(text):
    if not new_text:
        new_text += char
        count +=1
        continue
    elif char == text[i - 1]:
        if i == len(text) - 1:
            count += 1
            new_text += str(count)
        count +=1
        continue
    else:
        if i == len(text) - 1:
            count += 1
            new_text += str(count)
        else:
            new_text = new_text+str(count)+char
            count = 1
print(new_text)
