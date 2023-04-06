import pytest
from module21.workshop.utils import add, division, f


@pytest.mark.parametrize('a, b, expect', [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expect):
    assert add(a, b) == expect


@pytest.mark.parametrize('x, expectError', [
    ('1', TypeError),
    ([1], TypeError),
    ((1,), TypeError)
])
def test_f(x, expectError):
    with pytest.raises(expectError):
        f(x)


@pytest.fixture
def connect():
    with open('test.txt', 'a') as f:
        f.write('test')



def test_division_by_zero(connect):
    # connect()
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

@pytest.fixture
def setup():
    x = [1, 2, 3]
    return x

def test_fixture(setup):
    assert len(setup) == 3
    assert setup == [1, 2, 3]


class Auth():
    def __init__(self):
        login = self.login
        password = self.password

@pytest.fixture()
def auth():
    t = Auth(login, password)

def test_ulmart(auth):
    auth_key = Auth.key
    r = requests.get(url, headers={'Authorization':auth_key})


