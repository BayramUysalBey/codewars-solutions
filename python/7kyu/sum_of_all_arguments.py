"""Write a function that finds the sum of all its arguments.

eg:

sum_args(1, 2, 3) # => 6
sum_args(8, 2) # => 10
sum_args(1, 2, 3, 4, 5) # => 15
TIPS:
ruby/python : http://lmgtfy.com/?q=Ruby+splat+operator

JS/Coffeescript : http://lmgtfy.com/?q=Javascript+arguments+variable

C: https://www.geeksforgeeks.org/variadic-functions-in-c/"""

# My solution
def sum_args(*arg):
    res = 0
    for num in arg:
        res += num
    return res

# My updated solution
def sum_args(*arg):
    return sum(num for num in arg)