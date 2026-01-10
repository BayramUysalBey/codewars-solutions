"""Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial"""

# My solution
import math
def factorial(n):
    if n == 0:
        return 1
    elif n < 0 or n > 12:
        raise ValueError
    else:
        return math.factorial(n)

# My updated solution
import math
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return math.factorial(n)