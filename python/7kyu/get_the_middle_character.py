'''You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"'''

# My solution
def get_middle(s):
    length = len(s)
    middle = length // 2
    for char in s:
        if length % 2 == 1:
            return s[middle:middle+1]
        elif length % 2 == 0:
            return s[middle-1:middle+1]
        
# My updated solution
def get_middle(s):
    length = len(s)
    middle = length // 2    
    if length % 2 == 0:
        return s[middle - 1:middle + 1]
    return s[middle]