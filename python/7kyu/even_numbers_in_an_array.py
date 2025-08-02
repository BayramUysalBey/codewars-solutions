"""Given an array of numbers, return a new array of length number containing the last even numbers from the original array (in the same order). The original array will be not empty and will contain at least "number" even numbers.

For example:

([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [4, 6, 8]
([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) => [-8, 26]
([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]"""

# My solution
def even_numbers(arr,n):
	result = []
	for char in arr:
		if char % 2 == 0:
			result.append(char)

	return result[-n:]

# My updated solution
def even_numbers(arr,n):
    return [char for char in arr if char % 2 == 0][-n:]