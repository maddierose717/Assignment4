import sys
import readline
from typing import List
from app.calculator import Calculation, CalculationFactory

def display_help() -> None:
    help_message = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Supported operations:
        add
        subtract
        multiply
        divide

Special Commands:
    help
    history
    exit

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
"""
    print(help_message)
