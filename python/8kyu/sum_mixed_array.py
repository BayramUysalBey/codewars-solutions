"""Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number."""

# My solution
def sum_mix(arr):
	res = []
	for ey in arr:
		if type(ey) == str:
			res.append(int(ey))
		elif type(ey) == int:
			res.append(ey)
	return sum(res)

# My updated solution
def sum_mix(arr):
    return sum(map(int, arr))