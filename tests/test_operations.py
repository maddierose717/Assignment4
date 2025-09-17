import pytest
from app.operations import addition, subtraction, multiplication, division


def test_addition():
    assert addition(1, 1) == 2
    assert addition(-2, 5) == 3
    assert addition(0, 0) == 0
    assert addition(1.5, 2.5) == 4.0


def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(-2, -2) == 0
    assert subtraction(-5, 3) == -8
    assert subtraction(2.5, 1.0) == 1.5


def test_multiplication():
    assert multiplication(3, 4) == 12
    assert multiplication(-2, 5) == -10
    assert multiplication(0, 10) == 0
    assert multiplication(2.5, 2) == 5.0


def test_division():
    assert division(10, 2) == 5
    assert division(-9, 3) == -3
    assert division(7.5, 2.5) == 3.0


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

