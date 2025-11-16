"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        c=b/a
        return c
    except ZeroDivisionError:
        return "Division by zero"
def logarithm(a,b):
    if a<0 or b<0:
        raise ValueError("Logarithm cannot be negative")
    return math.log(a,b)
def exponential(a,b):
    return a**b


