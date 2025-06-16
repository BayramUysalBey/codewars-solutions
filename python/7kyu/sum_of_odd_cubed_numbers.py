"""Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: Booleans should not be considered as numbers."""

# My solution
def cube_odd(arr):


    result = 0
    for n in arr:
        if type(n) != int:
            return None
        elif n % 2 != 0:
            result += (n ** 3)
        
            
    return result

# My updated solution
def cube_odd(arr):
    for n in arr:
        if type(n) != int:
            return None          
    return sum(n ** 3 for n in arr if n % 2 != 0)
