"""Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error"."""

# My solution
def problem(a):
	if type(a) is str:
		return "Error"
	else:
		return (a * 50) + 6

# My updated solution
def problem(a):
    return "Error" if a == str(a) else a * 50 + 6