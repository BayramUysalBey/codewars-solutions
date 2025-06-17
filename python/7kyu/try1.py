def cube_odd(arr):
    for n in arr:
        if type(n) != int:
            return None          
    return sum(n ** 3 for n in arr if n % 2 != 0)
