def is_leap_year(x):
    return x % 400 == 0 or (x % 100!= 0 and x % 4 == 0)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1990))