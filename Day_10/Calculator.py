from html.entities import name2codepoint
from Calculator_art import logo
from subprocess import run


def add(n1,n2):
    """Adds both parameters."""
    return n1+n2

def subtract(n1,n2):
    """Subtracts both parameters."""
    return n1-n2

def multiply(n1,n2):
    """Multiplies both parameters"""
    return n1*n2

def divide(n1,n2):
    """Divides both parameters"""
    return n1/n2

ops = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    run('clear')
    print(logo)

    num1 = float(input("What's the first number?: "))
    for key in ops:
        print(key)
    operation_symbol = input("Pick an operation from the options above: ")
    num2 = float(input("What's the second number?: "))
    first_answer = ops[operation_symbol](num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    while False if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.: ") == "n" else True:
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number?: "))
        second_answer = ops[operation_symbol](first_answer,num3)
        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        first_answer = second_answer

    while False if input(f"Are you done? Type 'y' or 'n': ") == "n" else True:
        calculator()

calculator()