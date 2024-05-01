"""
Transitive closure complexity analysis:

Time complexity:
    O(V^3)

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
    """
    n = len(adj_list)
    connected = [[False]*n for i in range(n)]

    for u in range(n):
        connected[u][u] = True
        for e in adj_list[u]:
            v = e[0]
            connected[u][v] = True
    
    for k in range(n):
        for u in range(n):
            for v in range(n):
                connected[u][v] = connected[u][v] or (connected[u][k] and connected[k][v])
    
    return connected