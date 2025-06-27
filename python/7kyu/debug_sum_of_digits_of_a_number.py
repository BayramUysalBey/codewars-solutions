"""Debug   function getSumOfDigits that takes positive integer to calculate sum of its digits. Assume that argument is an integer.

Example
123  => 6
223  => 7
1337 => 14"""

# My solution
def get_sum_of_digits(num):
    sum = 0
    digits = list(str(num))
    for x in digits:
        sum += int(x)
    return sum

# My updated solution
def get_sum_of_digits(num):
    return sum(int(x) for x in list(str(num)))