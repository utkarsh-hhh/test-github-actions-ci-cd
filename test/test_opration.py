import pytest
from src.math_operation import add, sub, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(10, -2) == 12

def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(-2, 5) == -10
    assert multiply(10, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(-8, 4) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)