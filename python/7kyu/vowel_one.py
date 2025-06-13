'''vowelOne
Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.

Examples:

vowelOne "abceios" -- "1001110"

vowelOne "aeiou, abc" -- "1111100100"'''

# My solution
def vowel_one(s):
    vowels = "aeiou"
    s = s.lower()
    result = ""
    for char in s:
        if char in vowels:
            result += str(1)
        else:
            result += str(0)
    return "".join(result)

# My updated solution
def vowel_one(s):
    vowels = "aeiou"
    return "".join("1" if char in vowels else "0" for char in s.lower())