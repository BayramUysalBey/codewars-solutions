"""Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
You can assume that all values are integers. Do not mutate the input array."""

# My solution
def invert(lst):
    res = []
    for ls in lst:
        if ls in lst:
            res.append(-1 * ls)
    return res

# My updated solution
def invert(lst):
    if lst is []: return []
    return [-1 * num for num in lst]