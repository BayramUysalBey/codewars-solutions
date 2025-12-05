"""Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0."""

# My solution
def find_average(numbers):
	if sum(numbers) > 0:
		return sum(numbers) / len(numbers)
	else:
		return 0

# My updated solution
def find_average(numbers):
    if numbers == []: return 0
    return sum(numbers) / len(numbers)