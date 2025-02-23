"""You get an array of numbers, return the sum of all of the positives ones.

Example
[1, -4, 7, 12] => 1+7+12=20
Note
If there is nothing to sum, the sum is default to 0."""

# My solution
def positive_sum(arr):
	return sum(num for num in arr if num > 0)