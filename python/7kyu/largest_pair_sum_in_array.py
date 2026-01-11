"""Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer."""

# My solution
def largest_pair_sum(numbers): 
    s_numbers = sorted(numbers, reverse = True)
    return s_numbers[0] + s_numbers[1]

# My updated solution
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])