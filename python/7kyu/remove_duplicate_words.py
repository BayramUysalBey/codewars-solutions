"""Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'"""

# My solution
def remove_duplicate_words(s):
    s = s.split()
    seen = set()
    result = []
    for word in s:
        if word not in seen:
            result.append(word)
            seen.add(word)
    return " ".join(result)