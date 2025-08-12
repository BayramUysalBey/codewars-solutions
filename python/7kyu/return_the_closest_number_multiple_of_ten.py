"""Given a number return the closest number to it that is divisible by 10.

Example input:

22
25
37
Expected output:

20
30
40"""

# My solution
def closest_multiple_10(i):
    result = i % 10
    if result < 5:
        return i - result
    elif result >= 5:
        return (i - result) + 10