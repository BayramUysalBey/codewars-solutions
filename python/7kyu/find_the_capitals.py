"""Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]"""

# My solution
def capitals(word):
    result = []
    for i, char in enumerate(word):
        if char.isupper():
            result.append(i)
    return result

# My updated solution
def capitals(word):
	return [i for i, char in enumerate(word) if char.isupper()]