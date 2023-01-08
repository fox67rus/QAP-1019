# Задание 14.2.5
# Дано натуральное число N. Вычислите сумму его цифр.
def rec_num_sum(num):
    if num < 10:
        return num
    return num % 10 + rec_num_sum(num // 10)

print(rec_num_sum(2))
print(rec_num_sum(12))
print(rec_num_sum(126))
