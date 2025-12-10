"""Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]"""

# My solution
def reverse_seq(n):
    res = []
    for n in range(1, n + 1):
        res.append(n)
    return res[::-1]

# My updated solution
def reverse_seq(n):
    return list(range(n, 0, -1))