"""This kata is about converting numbers to their binary or hexadecimal representation:

If a number is even, convert it to binary.
If a number is odd, convert it to hex.
Numbers will be positive. The hexadecimal string should be lowercased."""

# My solution
def evens_and_odds(n):
    if n % 2 == 0: return str(int(bin(n)[2:]))
    else: return str(hex(n).split('x')[-1])
    
# My updated solution
def evens_and_odds(n):
    return hex(n)[2:] if n % 2 else bin(n)[2:]