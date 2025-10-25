"""An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"""

# My solution
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    sorted_str1 = sorted(test)
    sorted_str2 = sorted(original)
    return sorted_str1 == sorted_str2

# My updated solution
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower()) 