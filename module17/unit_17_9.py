def binary_search(array, element, left, right):
    if left > right:
        return False

    if array[left] > element or element > array[right]:
        raise IndexError

    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


try:
    # Данные для ввода:
    # 4 5 8 7 9 6 5 2 1 4 5 8 5 77 85 5 2 3 6 4 8 9 8 5 7 4 5 2 1 3 2 9
    # 7 6 2 8 4 1 3 9 5 0
    num_array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
    search_element = int(input('Введите любое число: '))

    qsort(num_array, 0, len(num_array) - 1)
    print(num_array)
    print(binary_search(num_array, search_element, 0, len(num_array) - 1))
except ValueError as e:
    print('Некорректный ввод данных: принимаются только целые числа через пробел', e)
except IndexError:
    print('Введенное число, не соответствует условию поиска')
