import pytest


# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [10, 11])
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True

# @pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
# @pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True

def ids_x(val):
    return "x=({0})".format(str(val))


def ids_y(val):
    return "y=({0})".format(str(val))


@pytest.mark.parametrize("x", [-1, 0, 1], ids=ids_x)
@pytest.mark.parametrize("y", [100, 1000], ids=ids_y)
def test_multiply_params(x, y):
    print("x: {0}, y: {1}".format(x, y))
    assert True
