"""
Prim's algorithm for minimum spanning tree

Time and space complexity exactly the same as dijkstra's algorithm

Time complexity: (with priority queue, min_heap)
    adj_list: O(VLog(V) + ELog(V))
    adj_matrix: O(VLog(V) + ELog(V) + (V^2-E))

Aux space complexity:
    O(V) for the dist, pred arrays, and O(E) for the heap
    so, O(E+V)


"""


import math
import heapq

def prim_mst(G, r):
    """
    performs Prim's algorithm on a weighted graph G, to generate a minimum spanning tree.
    G: adj matrx representation of a graph
    r: root node to start from

    Also uses a min_heap to store vertices with dist values as keys.
        - Unlike Dijktra's algorithm where the dist = path distance from s to v
            - at each iteration a the closest vertex is popped and 
                all its edges are checked for closer paths
                and any node that had its distance updated is pushed in

        - Prim's algorithm dist = minimum edge connecting v.
            - at each iteration the vertex with the smallest/lightest edge is popped and
                the vertex is connected in the Tree based on this edge 
                and then all the edges of this vertex is added into the heap
        * Note: both update the dists in the heap by pushing in a new value with a lower distance,
                - the old entry that has a higher dist is considered outdated and not processed.
    
    """
    dist = [math.inf] * len(G)
    visited = [False] * len(G)
    parent = [None] * len(G)
    dist[r] = 0
    
    # formally all the vertices are initially pushed in with math.inf dist values,
    # and the dists are to be updated throughout algorithm. However our implementation does not need this
    min_heap = [(dist[r], r)] 
    heapq.heapify(min_heap)

    while min_heap:
        key, u = heapq.heappop(min_heap)
        if key == dist[u]: # if dist up to date, is the minimum edge to u from parent[u]
            visited[u] = True
            for e in G[u]: # for all the edges coming out from the node
                v = e[0]
                w = e[1]
                if not visited[v] and dist[v] > w:
                    dist[v] = w # dist = edge weight, instead of path length like in dijkstras
                    parent[v] = u
                    heapq.heappush(min_heap, (dist[v], v))
    
    return dist, parent
