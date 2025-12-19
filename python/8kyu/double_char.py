"""Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* 'String'      -> 'SSttrriinngg'
* 'Hello World' -> 'HHeelllloo  WWoorrlldd'
* '1234!_ '     -> '11223344!!__  '"""

# My solution
def double_char(s):
	character_list = []
	for character in s:
		character_list += [character * 2]
	return "".join(character_list )

# My updated solution
def double_char(s):
    return ''.join(character * 2 for character in s)