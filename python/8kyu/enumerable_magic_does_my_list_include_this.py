"""Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false."""

# My solution
def include(arr, item):
    if item in arr:
        return True
    else:
        return False

# My updated solution
def include(arr,item):
    return item in arr