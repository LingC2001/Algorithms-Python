"""
Minimum cut complexity analysis:
These are same as the maximum flow problem. Refer to ford_fulkerson.py for details.

Time complexity:
    O(E*max_flow)

Aux space complexity:
    O(V + E)

"""

from ford_fulkerson import ford_fulkerson

def minimum_cut(adj_list, source, sink):
    """
    Finds the minimum cut of a network, as well as returns the S/T sets of
    the nodes.
    Where S = all nodes on the source side of the min cut.
    Where T = all nodes on teh sink side of the min cut.
    The minimum cut is the total edge weight of all edges cross from nodes in S to nodes in T.
    
    Note that S can be easily found, as it is just all the nodes that are reachable
    from source (via an edge with residual >0) in the residual graph. This is because
    the minimum cut will occur on the edges that are fully saturated. Hence residual = 0.
    
    T would be all the nodes that are left
    """
    n = len(adj_list)
    max_flow, final_res_graph = ford_fulkerson(adj_list, source, sink)

    # find all nodes reachable from s.
    S = set()
    dfs(final_res_graph, [False]*n, source, S)

    # find all nodes in T
    T = set()
    for i in range(n):
        if i not in S:
            T.add(i)
    
    return max_flow, S, T

def dfs(res_graph, visited, u, reachable):
    visited[u] = True
    reachable.add(u)
    
    for e in res_graph[u]:
        v = e.next
        residual = e.cap - e.flow
        if residual > 0 and not visited[v]:
            dfs(res_graph, visited, v, reachable)
