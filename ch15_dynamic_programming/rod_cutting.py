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
    Helper method for top-down with memoized approach
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

def bottom_up_cut_rod(prices, n):
    """
    Bottum-up method
    solving any par- ticular subproblem depends only on solving “smaller” subproblems
    """
    r = [0 for i in range(n + 1)]
    for j in range(1, n + 1):
        q = -sys.maxsize-1
        for i in range(0, j):
            q = max(q, prices[i] + r[j - i - 1])
        r[j] = q
    print(r)
    return r[n]

def extended_bottom_up_cut_rod(prices, n):
    r = [0 for i in range(n + 1)]
    s = [0 for i in range(n + 1)]
    for j in range(1, n + 1):
        q = -sys.maxsize-1
        for i in range(0, j):
            if q < prices[i] + r[j - i - 1]:
                q = prices[i] + r[j - i - 1]
                s[j] = i + 1
        r[j] = q
    #print(r)
    print(s)
    #print(r[n])
    return (r, s, r[n])

def print_cut_rod_solution(p, n):
    (r, s, opt_val) = extended_bottom_up_cut_rod(p, n)
    i = n
    while i > 0:
        print("Make a cut of: " + str(s[i]))
        i = i - s[i]
    print("Highest price is: " + str(opt_val))
        
    
print_cut_rod_solution([1, 5, 8, 9, 10, 17, 17, 20], 4)
