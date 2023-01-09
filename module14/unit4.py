import time
def decorator_time(fn):
    def wrapper():
        average_time = 0
        print(f"Запустилась функция {fn}")
        for launch in range(100):
            t0 = time.time()
            result = fn()
            dh = time.time() - t0
            average_time = average_time + dh
        average_time /= 100

        print(f"Функция выполнилась 100 раз. Среднее время: {average_time:.10f}")
        return average_time  # задекорированная функция будет возвращать время работы

    return wrapper


def pow_2():
    return 10000000000000000000000000000000000000000000000 ** 1000


def in_build_pow():
    return pow(10000000000000000000000000000000000000000000000, 1000)

pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
in_build_pow()