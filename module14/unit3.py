import time
def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


for num in fib():
    print(num)
    time.sleep(1)