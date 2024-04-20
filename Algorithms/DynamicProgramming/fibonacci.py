"""
DP fibonacci complexity analysis

Time complexity:
    The number of subproblems/number cells in the memo table is O(n)
    For each subproblem, we just look at 2 previous subproblems, therefore O(1)
    So therefore it is O(n) total

Space complexity:
    In fibonacci top down, we cannot use the space saving trick, therefore
    we have to keep the entire memo table, therefore O(n)
    In fibonacci bottom up, currently it is also O(n) since we have the
    entire memo table, however, we notice that each subproblem only uses
    the previous 2 subproblems and the order in which we compute subproblems is
    we compute the smaller first.
        Threfore we can optimize space by only keeping the last 2 subproblems,
        reducing space complexity to O(1)

"""


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