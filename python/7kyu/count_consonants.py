"""Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u."""

# My solution
def consonant_count(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# My updated solution
def consonant_count(s):
    return sum(1 for char in s if char.isalpha() and char not in "aeiouAEIOU")