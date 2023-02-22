for a in range(1, 8):
    for b in range(1, 8):
        for c in range(1, 10):
            if a + b + c == 13:
                print(f'{a=}, {b=}, {c=}, {a * b * c=}')
