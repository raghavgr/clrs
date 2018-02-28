import sys
"""
Consider the following length and prices table:

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

Given a rod of length n, determine the maximum value
obtainable by cutting it up and selling the pieces.
For example, 
when n = 8, optimal value is 22, with pieces of length 6 and 2.
"""

def cut_rod(prices, n):
    """
    recursive.
    O(2^n)
    """
    if n == 0:
        return 0
    q = -sys.maxsize - 1
    for i in range (1, n):
        q = max(q, prices[i] + cut_rod(prices, n - i))
    return q 

