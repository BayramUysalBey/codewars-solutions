"""Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar."""

# My solution
def is_palindrome(s):
    res = s.lower()
    if res == res[::-1]:
        return True
    elif res == " ":
        return True
    else:
        return False
    return res

# My updated solution
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]