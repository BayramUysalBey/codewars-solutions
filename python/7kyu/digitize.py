"""Given a non-negative integer, return an array / a list of the individual digits in order.

Examples:

123 => [1,2,3]

1 => [1]

8675309 => [8,6,7,5,3,0,9]"""

# My solution
def digitize(n):
    res = []
    n_str = str(n)
    for char in n_str:
        res.append(int(char))
    return res

# My updated solution
def digitize(n):
    return [int(char) for char in str(n)]