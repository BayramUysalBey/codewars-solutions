"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)"""

# My solution
def is_isogram(string):
    string = string.lower()
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True

# My updated solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))