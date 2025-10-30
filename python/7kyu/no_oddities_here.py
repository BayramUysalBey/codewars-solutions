"""Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given."""

# My soution
def no_odds(values):
    result = []
    for char in values:
        if char % 2 == 0:
            result.append(char)
    return result

# My updated solution
def no_odds(values):
    return [char for char in values if char % 2 == 0]