# Задание 14.5.10
# Напишите рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули
def rec_reverse_num(num):
    if num < 10:
        return num
    number_of_tens = len(str(num)) - 1

    return num % 10 * 10 ** number_of_tens + rec_reverse_num(num // 10)


print(rec_reverse_num(35))
print(rec_reverse_num(135))
print(rec_reverse_num(2135))

