"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"""

# My solution
def reverse_words(text):
    s_text = text.split(" ")
    res = []
    for word in s_text:
        res.append(word[::-1])
    return " ".join(res)

# My updated solution
def reverse_words(text):
    return " ".join(t[::-1] for t in text.split(" "))