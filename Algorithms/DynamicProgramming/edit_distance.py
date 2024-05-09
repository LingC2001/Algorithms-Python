"""
Edit Distance complexity analysis

Time complexity:
    There are n*m subproblems.
    Each subproblem looks at 3 previous subproblems.
    Therefore O(nm)

Space complexity:
    DP memo table size: O(nm)
    * Notice how each subproblem only looks at subproblems from previous
      cols and the previous row, therefore we can optimize by only keeping
      2 rows of the table. If we always choose the smaller string to be the row,
      then it will be O(min(n,m))
    * Note that you can no longer backtrack to reconstruct answer if we do this.

"""


def edit_distance(string1, string2):
    m, n = len(string1), len(string2)
    
    # Create a table to store results of sub-problems
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # Initialize the table
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    # Fill the table in bottom-up manner
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If last characters are same, ignore last character
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # If last characters are different, consider all possibilities
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]