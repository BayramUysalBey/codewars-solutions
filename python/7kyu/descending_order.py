"""Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321"""

# My solution
def descending_order(num):
    n_list = list(str(num))
    n_list.sort(reverse=True)
    return int(''.join(n_list))

# My updated solution
def Descending_Order(num):
	return int("".join(sorted(str(num), reverse=True)))


