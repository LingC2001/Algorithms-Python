"""
Kahn's algorithm for topological sorting

Given a DAG (directed acyclic graph)
Notice how in topological order, we start with the nodes where there are no incoming edges
and end on nodes with no outgoing edges.
Kahn's algorithm uses this fact and maintains a queue of vertices ready to be inserted into 
the sorted list. A vertex is considered ready when it has no incoming edges. When a vertex is
inserted, all outgoing edges of it are removed, so that the next item in topological order
would have no more incoming edges.

Note that the in_degree (number of incoming edges) of each node can be calculated,
and when an incoming edge is removed, reduce the in_degree by 1. This is more efficient
than actually removing the edge in the graph.

Time Complexity:
    Every vertex is process once, and all the outgoing edges of the vertex are checked and removed.
    This is O(V + E) when using adjacency list, and O(V^2) when using adjacency matrix

    For the initial indegree calculation of every node, every edge is checked.
    Therefore O(V) for creating V-size zero list, O(E) checking every edge, using adj_list
    If using adj_matrix, O(V) for creating V-size zero list, O(V^2) for checking every edge

    Combined:
        adj_list: O(2V + 2E)
        adj_matrix: O(V + 2V^2)

Space complexity:
    O(V) for order, queue and in_degree

"""


from collections import deque

def topological_sort_khan(adj_list):
    """
    given a directed acyclic graph
    """
    order = []
    ready = deque()
    in_degree = calculate_in_degree(adj_list)
    # add all vertices with no incoming edges
    
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            ready.append(i)


    while ready:
        u = ready.popleft()
        order.append(u)
        for v in adj_list[u]:
            # remove edge (don't need to actually delete it if using in degree method)
            in_degree[v] -= 1

            if in_degree[v] == 0:    
                ready.append(v)
                    
    return order

def calculate_in_degree(adj_list):
    n = len(adj_list)
    in_degree = [0] * n

    for i in range(n):
        for v in adj_list[i]:
            in_degree[v] += 1
    return in_degree
