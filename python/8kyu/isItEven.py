"""In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is even (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, integers or floats.

Floats with decimal part non equal to zero are considered UNeven for this kata."""

# My solution
def is_even(n): 
    # your code here
    return abs(n) % 2 == 0 and isinstance(n, int) or isinstance(n, float) and abs(n) - int(abs(n)) == 0