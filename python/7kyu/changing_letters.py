"""When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata."""

# My solution
def swap(st):
	
	vowels = "aeiou"
	result = []
	for char in st:
		if char in vowels:
			result.append(char.upper())
		else:
			result.append(char)
	return "".join(result)

# My updated solution
def swap(st):
    return "".join((char.upper()) if char in "aeiou" else char for char in st)