"""You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle"""

# My solution
def other_angle(a, b):
    res = 180 - (a + b)
    return res

# My updated solution
def other_angle(a, b):
    return 180 - (a + b)