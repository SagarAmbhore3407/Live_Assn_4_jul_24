
#12. Write a Python module named calculator.py containing functions for addition, subtraction, 
#    multiplication, and division.

# calculator.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers. Raise an error if the divisor is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


