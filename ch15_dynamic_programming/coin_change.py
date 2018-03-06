"""
Use dynamic approach to solve coin change problem.
Given the change required, and the available coin
denominations, return the least number of coins required
to give the change.

Ex:
Change = 63
Coin Denominations available = 1, 5, 10, 25
Sol: 25 + 25 + 10 + 1 + 1 + 1

Greedy approach used above. If coin denomination had 21,
then greedy approach won't work as the optimal solution
is three 21 coins.
"""

def recurCoinChange(coinValList, change):
    """
    Recursive solution with no memoization.
    Costs a lot
    """
    minCoins = change
    if change in coinValList:
        return 1
    else:
        for i in [c for c in coinValList if c <= change]:
            numCoins = 1 + recurCoinChange(coinValList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

def recurCoinChangeMemo(coinValList, change, knownResults):
    """
    Recursive solution with memoization.
    Does not give optimal solution
    """
    minCoins = change
    if change in coinValList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValList if c <= change]:
            numCoins = 1 + recurCoinChangeMemo(coinValList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

def dpMakeChange(coinValList, change, minCoins):
    """
    Dynamic programming version
    Returns optimal value but not the solution
    """
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValList if c <= change]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
        #print(minCoins)
    
    return minCoins[change]

def extended_dpMakeChange(coinValList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValList if c <= change]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    printCoins(coinsUsed, change)
    return minCoins[change]

def printCoins(coinsUsed, change):
    print(coinsUsed)
    remaining = change
    while remaining > 0:
        curr = coinsUsed[remaining]
        print(curr)
        remaining -= curr
print(extended_dpMakeChange([1, 5, 10], 11, [0]*12, [0]*12))
print(extended_dpMakeChange([2], 3, [0]*4, [0]*4))


