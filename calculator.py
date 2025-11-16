"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
<<<<<<< HEAD
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero: 'a' is 0")
    return a / b

def log(a, b):
    if a < 0 or b < 0:
        raise ValueError("Log values cannot be negative")
    return math.log(a, b)

def exp(a, b):
    return a ** b


import math
def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError("a<0")
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except:
        raise ValueError("can't have negative nums")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a,b):
    if a<0 or b<0:
        raise ValueError("Logarithm cannot be negative")
    return math.log(a,b)
def exponential(a,b):
    return a**b



