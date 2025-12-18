"""Complete the solution so that it reverses all of the words within the string passed in.

Words are separated by exactly one space and there are no leading or trailing spaces.

Example(Input --> Output):

'The greatest victory is that which requires no battle' --> 'battle no requires which that is victory greatest The'"""

# My solution
def reverse_words(s):
    res = s.split()
    res1 = (res[::-1])
    return " ".join(res1)

# My updated solution
def reverse_words(s):
    s_split = s.split()
    return " ".join(s_split[::-1])