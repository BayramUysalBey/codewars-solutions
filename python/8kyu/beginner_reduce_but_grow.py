"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""

# My solution
def grow(arr):
    res = 1
    for a in arr:
        if a in arr:
            res *= a
    return res