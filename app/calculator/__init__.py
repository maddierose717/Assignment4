from abc import ABC, abstractmethod
from app.operations import Operations


class Calculation(ABC):
    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b

    @abstractmethod
    def execute(self) -> float:
        pass  # pragma: no cover

    def __str__(self) -> str:
        result = self.execute()
        operation_name = self.__class__.__name__.replace('Calculation', '')
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(a={self.a}, b={self.b})"
    
    class CalculationFactory:
        _calculations = {}
    
        @classmethod
        def register_calculation(cls, calculation_type: str):
            def decorator(subclass):
                calculation_type_lower = calculation_type.lower()
                if calculation_type_lower in cls._calculations:
                    raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
                cls._calculations[calculation_type_lower] = subclass
                return subclass
            return decorator
    
        @classmethod
        def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
            calculation_type_lower = calculation_type.lower()
            calculation_class = cls._calculations.get(calculation_type_lower)
            if not calculation_class:
                available_types = ', '.join(cls._calculations.keys())
                raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available_types}")
            return calculation_class(a, b)

