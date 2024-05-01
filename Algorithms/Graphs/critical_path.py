"""
Critical path complexity analysis

Time complexity:
    The number of subproblems is the number of nodes
    Each subproblem is solved by checking all its edges
    Bottom up:
        Finding reverse topological order O(V+E)
        We set initial dp table to zeros, therefore base case already done
        checking all edges of every node O(V+E)

    Top down:
        Finding out degree and setting base case: O(V)
        checking all edges of every node O(V+E)

Auxiliary space complexity:
    O(V) for dp table
    
"""

def critical_path_memo(adj_list, memo, u):
    """
    The critical path problem is also the problem of finding the longest path
    in a DAG(directed acyclic graph). If we consider the nodes to be tasks to be
    done in topological order, then the critical path is the path that takes
    the longest to finish and has no slack. 

    This problem has a simple recurrence relation, where the base case is the last
    node (node with no outgoing edges) has a dist of 0. Therefore the node before
    the last node must be the edge with the highest weight.
        dp[u] = max(w(u,v) + dp[v]) for all nodes v that have an edge from u.
    

    Note that the order of the subproblems is solved in order of reverse topological 
    order. Computing the topological order using dfs is O(V+E). Therefore we might as
    well do top-down dynamic programming approach since we don't know the order of the
    subproblems easily.

    Note that performing top-down recursive approach is essentially the same as 
    performing a dfs on the subproblem graph and producing a reverse topological order
    as a by-product.
    
    """
    if memo[u] is None:
        memo[u] = 0
        for e in adj_list[u]:
            v = e[0]
            w = e[1]
            memo[u] = max(memo[u], w + critical_path_memo(adj_list, memo, v))

    return memo[u]


def critical_path(adj_list):
    n = len(adj_list)
    longest = [None]*n

    # finding edges with out-degree of 0 and setting base case
    out_degree = [len(adj_list[u]) for u in range(n)]
    for u in range(n):
        if out_degree[u] == 0:
            longest[u] = 0
    
    for u in range(n):
        if longest[u] is None:
            critical_path_memo(adj_list, longest, u)

    return max(longest)