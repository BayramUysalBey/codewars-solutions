"""Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'"""

# My solution
def switcheroo(s):
    res = []
    s = list(s)
    for char in s:
        if char == "a":
            res.append("b")
        elif char == "b":
            res.append("a")
        elif char == "c":
            res.append("c")
    return "".join(res)

# My updated solution
def switcheroo(s):
	bundle = {"a": "b",
		   "b": "a",
			"c": "c"
			}
	return "".join(bundle[char] for char in s)