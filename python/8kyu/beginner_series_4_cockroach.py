"""The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer."""

# My solution
from math import *

def cockroach_speed(s):
    res = s * 27.777778
    return floor(res)

# My updated solution
from math import floor
def cockroach_speed(s):
    return floor(s * 27.777778)