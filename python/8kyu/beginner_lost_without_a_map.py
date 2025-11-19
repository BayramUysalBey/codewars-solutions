"""Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]"""

# My solution
def maps(a):
    res = []
    for b in a:
        if b in a:
            res.append(b * 2)
    return res

# My updated solution
def maps(a):
    return [x * 2 for x in a]