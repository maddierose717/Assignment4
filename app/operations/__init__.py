from typing import Union

Number = Union[int, float]


class Operations:
    @staticmethod
    def addition(a: Number, b: Number) -> Number:
        return a + b

    @staticmethod
    def subtraction(a: Number, b: Number) -> Number:
        return a - b

    @staticmethod
    def multiplication(a: Number, b: Number) -> Number:
        return a * b

    @staticmethod
    def division(a: Number, b: Number) -> Number:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

