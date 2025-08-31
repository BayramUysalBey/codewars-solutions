"""Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not."""

# My solution
import string
def is_it_letter(s):
    letter = "".join(string.ascii_letters)
    for char in s:
        if char in letter: return True
        else: return False
        
# My updated solution
def is_it_letter(s):
    return s.isalpha()