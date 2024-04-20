"""
matrix multiplication order complexity analysis

Time complexity:
    There are O(n^2) subproblems. 
    Each subproblem requires checking all the splits inbetween i and j
    It can be proven to be O(n^3)

Space complexity:
    dp table size: O(n^2)

"""

import math
def matrix_order(matrices):
    n = len(matrices)
    if n <= 1:
        return 0
    
    dp = [[0]*n for i in range(n)]
    # dp[i][j] = minimum cost for multiplying matrices[i]*matrices[i+1]*...*matrices[j]

    for length in range(2, n+1):
        # for all starting indices:
        # the maximum starting index i when length = 1 should be n-1
        # the maximum starting index i when length = n should 0
        for i in range(n-length+1): 
            j = i+length-1 # when i = 0, length = 2, j = 1, because j is inclusive
            best = math.inf
            
            # for all possible split points between i and j: 
            # (matrix k is included in the first half split)
            # e.g if i = 0, j = 5, k = 2, then you are performing the split: [0, 1, 2] * [3, 4, 5]
            for k in range(i, j):
                multiplication_cost = matrices[i][0]*matrices[k][1]*matrices[j][1]
                best = min(best, dp[i][k]+dp[k+1][j]+ multiplication_cost)
            dp[i][j] = best
    return dp[0][n-1]