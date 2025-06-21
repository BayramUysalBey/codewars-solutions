"""Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types."""

# My solution
def find_short(s):
	s_s = s.split()
	for word in s_s:
		return len(min(s_s, key=len))
	
# My updated solution
def find_short(s):
    return len(min(s.split(), key=len))