"""Failed Filter - Bug Fixing #3
Oh no, Timmy's filter doesn't seem to be working? Your task is to fix the Filter Number function to remove all the numbers from the string."""

# My solution
def filter_numbers(string):
	nums = "0123456789"
	result = []
	
	for x in string:
		if x not in nums:
			result.append(x)
	return "".join(result)

# My updated solution
def filter_numbers(string):
	nums = "0123456789"
	return "".join(x for x in string if x not in nums)