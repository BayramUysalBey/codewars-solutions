"""Debug the functions
Should be easy, begin by looking at the code. Debug the code and the functions should work."""

# My solution
def multi(l_st):
    res = 1
    for x in l_st:
        res *= x
    return res

def add(l_st):
    res = 0
    for x in l_st:
        res += x
    return res

def reverse(st):
    return st[::-1]

# My updated solution
def multi(l_st):   
	count = 1
	for x in l_st:
		count *= x
	return count

def add(l_st):
    return sum(l_st)

def reverse(st):
    return st[::-1]
