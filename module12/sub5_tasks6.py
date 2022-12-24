# списки
L = list(map(int, input("Введите числа через пробел: ").split()))

L[0], L[-1] = L[-1], L[0]
L.append(sum(L))
print(L)

