"""
Transitive closure complexity analysis:

Time complexity:
    Uses same principal as Floyd-Warshall, therefore O(V^3)

Aux Space complexity:
    O(V^2)
    - We make a boolean matrix, instead of integer so we can save space.
    Since each boolean value is only 1 byte.


"""

def transitive_closure(adj_list):
    """
    Given a directed graph, determines if any vertex v is reachable from any vertex u.
    The reachability matrix is called the transitive closure of a graph.
    Where there is an edge between u and v (connected[u][v]=True) if v is reachable from u.

    The idea is we perform Floyd-Warshall on a graph, doesn't matter the edge weights, assume all are 1.
    At the end of the algorithm, if dp[u][v] has a distance value that is not inf, then that means
    there must be a path from u->v.

    Since we only care about if they are connected or not, we can just keep a boolean value.
    If u->k is reachable and k->v has an edge/is reachable, then u->v must be reachable.

    """
    n = len(adj_list)
    connected = [[False]*n for i in range(n)]

    # base cases, if there is an edge between u->v, then v is reachable from u.
    for u in range(n):
        connected[u][u] = True
        for e in adj_list[u]:
            v = e[0]
            connected[u][v] = True
    
    # Floyd-Warshall
    for k in range(n):
        for u in range(n):
            for v in range(n):
                connected[u][v] = connected[u][v] or (connected[u][k] and connected[k][v])
    
    return connected