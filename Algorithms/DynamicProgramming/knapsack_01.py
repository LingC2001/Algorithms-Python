"""
knapsack 01 complexity analysis:

Time complexity:
    The number of subproblems is n*C
        it finds the max value for each capacity for all items up until i.
        e.g. the first row contains all the max values for only using the first item
        the second tow contains all the max values for only using the items 1-2
        - Each subproblem only looks at

Space complexity:
    The memo table is O(nC)
    However notice how the each subproblem strictly only requires the previous row.
    So if we do bottom up approach, we can compute the memo table one row at a time
    and only ever store 2 rows of the dp table in memory. Hence O(C) is achieveable

"""


def knapsack_01(values, weights, capacity):
    n = len(values)
    if n == 0 or capacity <= 0:
        return 0
    
    max_values = [ [0]*(capacity+1) for i in range(n+1) ]

    for i in range(1, n+1):
        item_idx = i-1 # because we have an extra initial row in max_values for no items
                       # so our item index is shifted compared to in memoisation table
        for c in range(capacity+1):
            if weights[item_idx] <= c:
                max_values[i][c] = max(max_values[i-1][c], values[item_idx]+max_values[i-1][c-weights[item_idx]])
            else:
                max_values[i][c] = max_values[i-1][c]
    return max_values[n][capacity]
