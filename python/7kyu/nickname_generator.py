"""Nickname Generator

Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

If the 3rd letter is a consonant, return the first 3 letters.

nickname("Robert") //=> "Rob"
nickname("Kimberly") //=> "Kim"
nickname("Samantha") //=> "Sam"
If the 3rd letter is a vowel, return the first 4 letters.

nickname("Jeannie") //=> "Jean"
nickname("Douglas") //=> "Doug"
nickname("Gregory") //=> "Greg"
If the string is less than 4 characters, return "Error: Name too short".

Notes:

Vowels are "aeiou", so discount the letter "y".
Input will always be a string.
Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
The input can be modified"""

# My solution
def nickname_generator(name):
    if len(name) <= 3:
        return "Error: Name too short"
    letter = "aeiou"
    char = name[2]
    result = ""
    
    if char in letter:
        result += name[:4]
    else:
        result += name[:3]
    return result

# My updated solution
def nickname_generator(name):
    if len(name) <= 3:
        return "Error: Name too short"
    
    vowels = "aeiou"
    third_char = name[2]
    
    if third_char in vowels:
        return name[:4]
    else:
        return name[:3]
    
# My updated solution - II
def nickname_generator(name):
    return "Error: Name too short" if len(name) <= 3 else name[:3+(name[2] in "aeiuo")]