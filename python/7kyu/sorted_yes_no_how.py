"""Complete the method which accepts an array of integers, and returns one of the following:

"yes, ascending" - if the numbers in the array are sorted in an ascending order
"yes, descending" - if the numbers in the array are sorted in a descending order
"no" - otherwise
You can assume the array will always be valid, and there will always be one correct answer."""

# My solution
def is_sorted_and_how(arr):
	s_arr = sorted(arr, reverse=True)
	s_arr1 = sorted(arr, reverse=False)


	if arr == s_arr:
		return "yes, descending"
	elif arr == s_arr1:
		return "yes, ascending"
	else:
		return "no"

# My updated solution
def is_sorted_and_how(arr):
	if arr == sorted(arr, reverse=True):
		return "yes, descending"
	elif arr == sorted(arr, reverse=False):
		return "yes, ascending"
	else:
		return "no"