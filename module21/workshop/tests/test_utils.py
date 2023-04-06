import pytest
from module21.workshop.utils import add, division

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)
