"""Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters."""

# My solution
def has_unique_chars(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True

# My updated solution
def has_unique_chars(string):
    return len(string) == len(set(string))