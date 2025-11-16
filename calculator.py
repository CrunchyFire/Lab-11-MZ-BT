#https://github.com/CrunchyFire/Lab-11-MZ-BT
#Partner 1: Michael Zhang
#Partner 2: Benjamin Thanapaisarnkij
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example

def add(a, b):
    return a + b



def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero: 'a' is 0")
    return b / a

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


def logarithm(a,b):
    if a<1 or b<0:
        raise ValueError("Logarithm cannot be negative")
    return math.log(a,b)



