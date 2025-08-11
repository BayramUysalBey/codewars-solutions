"""In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.

For example:

solve("xyab","xzca") = "ybzc" 
--The first string has 'yb' which is not in the second string. 
--The second string has 'zc' which is not in the first string. 
Notice also that you return the characters from the first string concatenated with those from the second string.

More examples in the tests cases.

Good luck!"""

# My solution
def solve(a,b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    for j in b:
        if j not in a:
            result.append(j)
    return "".join(result)