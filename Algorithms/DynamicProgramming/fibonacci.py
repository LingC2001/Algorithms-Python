
def fibonacci_top_down(n):
    memo = [None]*(n+1)
    return fibonacci_top_down_memo(n, memo)

def fibonacci_top_down_memo(n, memo):
    if n <= 1:
        return n # base case
    
    # skip computation if subproblem already solved before
    if memo[n] is None: # if the this subproblem (fib number) hasn't been found yet
        memo[n] = fibonacci_top_down_memo(n-1, memo) + fibonacci_top_down_memo(n-2, memo)

    # return from memo table
    return memo[n] 

def fibonacci_bottom_up(n):
    if n <= 1:
        return n

    memo = [0]*(n+1)
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]