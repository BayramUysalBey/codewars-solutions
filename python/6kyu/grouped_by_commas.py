'''Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n <= 2147483647

Examples
       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235" '''

# My solution
def group_by_comma(n):
    s = str(n)
    if len(s) <= 3:
        return s
    else:
        rev = s[::-1]
        groups = [rev[i:i+3] for i in range(0, len(rev), 3)]
        joined = ','.join(groups)
        result = joined[::-1]
        return result
    
# My updated solution
def group_by_commas(n):
    return f"{n:,}"