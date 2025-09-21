import pytest
from typing import Union
from app.operations import Operations 

number = Union[int, float]


@pytest.mark.parametrize("a, b, expected",

 [
        (2, 3, 5),           # Test adding two positive integers
        (0, 0, 0),           # Test adding two zeros
        (-1, 1, 0),          # Test adding a negative and a positive integer
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
     result = Operations.addition(a, b)
     assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

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
        
def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)
