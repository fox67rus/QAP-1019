# Убедитесь в этом самостоятельно, написав функцию p(n), вызывающую эту же самую функцию с аргументом,
# уменьшенным на единицу, и после чего печатающую значение аргумента.
# Обратите внимание на описанный порядок действий и наличие условие выхода из рекурсии.

def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)

p(6)