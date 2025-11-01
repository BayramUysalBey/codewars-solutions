"""Determine the total number of digits in the integer (n>=0) given as input to the function. For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

All inputs will be valid."""

# My solution
def digits(n):
	l_n = list(str(n))
	len_n = len(l_n)
	return len_n

# My updated solution
def digits(n):
	return len(str(n))
