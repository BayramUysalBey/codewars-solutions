"""Write a function that doubles every second integer in a list, starting from the left.

Example:

For input array/list :

[1,2,3,4]
the function should return :

[1,4,3,8]"""

# My solution
def double_every_other(lst):
    result = []
    for number in lst:
        if lst.index(number) % 2 != 0: result.append(number * 2)
        else: result.append(number)
    return result
print(double_every_other([2967, 1235, -1878, -948, 14, -1151, -2866, 1838, -1676, -408, -934, -1756, -1756, 250, -556, 2610, 2734, -2761, 686, -1505, 444]))

# My updated solution
def double_every_other(lst):
    return [number * 2 if i % 2 != 0 else number for i, number in enumerate(lst)]