"""Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number."""

# My solution
def div_con(x):
	res_s = 0
	res_i = 0
	for char in x:
		if type(char) == str:
			res_s += int(char)
		elif type(char) == int:
			res_i += char
	return res_i - res_s