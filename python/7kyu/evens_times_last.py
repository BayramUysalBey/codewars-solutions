"""Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.

Indices in sequence start from 0.

If the sequence is empty, you should return 0."""

# My solution
def even_last(numbers): 
    if numbers == [] : return 0
    result = 0
    for index, num in enumerate(numbers):
        if index % 2  == 0: result += num
    return result * numbers[-1]