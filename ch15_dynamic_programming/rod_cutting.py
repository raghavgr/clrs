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
    for i in range(n):
        q = max(q, prices[i] + cut_rod(prices, n - i))
    return q 

def memoized_cut_rod(prices, n):
    """
    Memoized cut rod. 
    Initialize r, an auxiliary array for revenue
    """
    r = [-1 for i in range(n)]
    return memoized_cut_rod_aux(prices, n, r)

def memoized_cut_rod_aux(prices, n, r):
    """
    Helper method for memoized approach
    top-down
    """
    if r[n- 1] >= 0:        # once result found, don't check again.
        return r[n - 1]
    if n == 0:
        q = 0
    else:
        q = -sys.maxsize - 1
        for i in range(0, n):
            q = max(q, prices[i] + memoized_cut_rod_aux(prices, n - i - 1, r))
    r[n - 1] = q
    return q

print(memoized_cut_rod([1, 5, 8, 9], 4))
