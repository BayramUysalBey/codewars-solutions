"""I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too."""

# My solution
def array_plus_array(arr1,arr2):
    r1 = sum(arr1)
    r2 = sum(arr2)
    return r1 + r2

# My updated solution
def array_plus_array(arr1,arr2):
    return sum (arr1 + arr2)