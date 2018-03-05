import sys
def matrix_chain(d):
    """
    d: a list of dimensions such that matrix i's dimensions 
        are d[i]-by-d[i + 1]
    """
    n = len(d) - 1      # number of matrices
    N = [[0] * n for i in range(n)]     # initialize n-by-n result to zero
    for b in range(1, n):               # number of products in subchain
        for i in range(n - b):
            j = i + b
            N[i][j] = sys.maxsize
            for k in range(i, j):
                q = N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if q < N[i][j]:
                    N[i][j] = q
    return N