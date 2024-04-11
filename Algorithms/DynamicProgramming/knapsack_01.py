
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
