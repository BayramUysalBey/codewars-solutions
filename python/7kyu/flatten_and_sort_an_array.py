"""Challenge:

Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9]."""

# My solution
def flatten_and_sort(array):
    if array == []:
        return []
    result = []
    for char in array:
        for num in char:
            result.append(num)
    return sorted(result)

# My updated solution
def flatten_and_sort(array):
    if array == []:
        return []
    return sorted([num for sublist in array for num in sublist])