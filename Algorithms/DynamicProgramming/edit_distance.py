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
    s1 = [c for c in string1]
    s2 = [c for c in string2]
    n = len(s1)
    m = len(s2)
    
    dist = [[0]*(m+1) for i in range(n+1)]

    # base case: If one string is empty, the number of edits must be
    # to insert/delete all the remaining characters
    for i in range(n+1):
        dist[i][0] = i
    for j in range(m+1):
        dist[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            # since there is an extra row and col in dp table, the indexing is shifted.
            # e.g. dist[1][1] is for 1 char left in s1 and s2, so therefore s1[0] and s2[0]
            chr1 = i-1 
            chr2 = j-1
            if s1[chr1] == s2[chr2]: # if the characters match, then no edits needed
                dist[i][j] = dist[i-1][j-1]
            else:
                # one edit is needed to be done, so +1.
                # if dist[i-1][j-1] is min, that means it is better to keep this alignment, and do REPLACEMENT
                # if dist[i-1][j] is min, that means removing the char from s1 is best alignment/insert char into s2 to match
                # if dist[i][j-1] is min, that means removing the char from s2 is best alignment/insert char into s1 to match
                dist[i][j] = min(dist[i-1][j-1], dist[i-1][j], dist[i][j-1]) + 1
    return dist[n][m]