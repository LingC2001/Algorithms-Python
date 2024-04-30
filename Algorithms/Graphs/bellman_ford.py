"""
Bellman Ford Complexity Analysis:

Time Complexity:
    We must perform V-1 iterations of checking all edges to guarantee correctness.
    Therefore time complexity is worst case: O(VE)
    We introducing early stopping for when no nodes gets distance improved.

Auxiliary Space complexity:
    O(V) for the dist/pred arrays

"""
import math

def bellman_ford(adj_list, s):
    """
    Perfroms Bellman-Ford algorithm to find the single source shortest path problem. 
    Finds the shortest path to all nodes from a starting node.
    Slower than Dijkstra's but works for graphs with negative edges or negative cycles.

    """
    n = len(adj_list)
    dist = [math.inf] * n
    pred = [None] * n
    dist[s] = 0

    for i in range(n-1): # perform V-1 iterations to guanrantee correctness
        # relax all edges
        improved = 0
        for u in range(n):
            for e in adj_list[u]:
                v = e[0]
                w = e[1]
                # relax
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    improved += 1
        if improved == 0:
            break

    
    # second iteration of Bellman-Ford to detect negative cycles
    for i in range(n-1): # perform V-1 iterations to guanrantee correctness
        # relax all edges
        improved = 0
        for u in range(n):
            for e in adj_list[u]:
                v = e[0]
                w = e[1]
                # relax
                if dist[u] + w < dist[v]:
                    # any edges than can be relaxed aka
                    # any nodes distances that can be improved must be reachable from a negative cycle
                    dist[v] = -math.inf
                    pred[v] = None
                    improved += 1
        if improved == 0:
            break
    
    return dist, pred
