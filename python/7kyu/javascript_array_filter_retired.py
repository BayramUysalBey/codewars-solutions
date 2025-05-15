"""In Python, there is a built-in filter function that operates similarly to JS's filter. For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter

The solution would work like the following:

get_even_numbers([2,4,5,6]) => [2,4,6]"""

# My solution
def get_even_numbers(arr):
    res = []
    for a in arr:
        if a % 2 == 0:
            res.append(a)
    return res

# My solution (update)
def get_even_numbers(arr):
    return [a for a in arr if a % 2 == 0]