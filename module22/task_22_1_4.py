# напишите функцию, которая определяет, можно ли составить треугольник из трёх отрезков,
# длины которых передаются в функцию.

import pytest


def is_triangle(a, b, c) -> bool:
    if a < b + c and b < a + c and c < a + b:
        return True
    return False

@pytest.mark.parametrize("a, b, c, expected", [
                        (3, 4, 5, True),
                        (450, 109, 467, True),
                        (-3, -4, -5, False),
                        (0, 0, 0, False),
                        (1, 2, 4, False),
                    ],)
def test_is_triangle(a, b, c, expected):
    print("a: {0}, b: {1}, c: {2}".format(a, b, c))
    assert is_triangle(a, b, c) == expected
