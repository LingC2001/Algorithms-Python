"""
Dijkstra's algorithm complexity analysis:

Time complexity: 
    In Dijkstra's algorithm, Each iteration we find the minimum distance node, and for all its
    edges we update the distances. Therefore the time complexity is simply: O(V*T_find + E*T_update)

    If we update the distances in only an array O(1), and find the minimum using array O(V), then the
    time complexity would be: O(V*V + E) = O(V^2)

    If we update the distances in an array as well as a min_heap O(log(V)), and pop the minimum from the
    min heap O(log(V)), then the time complexity would be: O(V*Log(V) + E*Log(V)) = O(ELog(V))
        - When we update distances in the heap, we just push in a new distance assosiated with the node, 
        and we ignore all other distances that does not match the new smallest distance stored in the array.
            This technically makes it so that the heap may grow to size E, so operations take O(log(E)), however
            since we have a simple graph, O(log(E)) = O(Log(V^2)) = O(2Log(V)) = O(Log(V)), so asymptotically is the same
    

    If a Fibonacci heap is used, we can acutally achieve O(E + VLog(V))

    Also technically using an adjacency list instead of an adjacency matrix would be faster 
    because we can just look at all the edges we have, and no need to use extra comparisons to 
    ignore all the zeros.
    adj_list: O(VLog(V) + ELog(V))
    adj_matrix: O(VLog(V) + ELog(V) + (V^2-E))
        - if the graph is dense where E ~= V^2, then it would be the same
        - but in a sparse graph where E ~= V, then it would make time complexity O(V^2) instead of O(VLog(V))



Aux space complexity:
    O(V) for the dist, pred arrays, and O(E) for the heap
    so, O(E+V)

"""

import heapq
import math
def dijkstra(G, s):
    """
    performs dijkstra's algorithm on a weighted graph G
    G is represented as a weighted adjacency list
        - the 
    s is the source
    
    When choose the next node to look at, Dijkstra's uses a min heap containing the distances.
    This means we choose to look at the closest(combined dists of path) node from 
    the starting node first. This means that Dijkstra's tries to minimise the length of the paths
    from the source/starting node.

    """
    dist = [math.inf] * len(G)
    pred = [None] * len(G)
    dist[s] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, s))

    while q:
        key, u = heapq.heappop(q)
        if key == dist[u]: # if distance is up to date
            for e in G[u]: # for all the edges coming out from the node
                # update the costs/dists using triangle inequality
                v = e[0]
                w = e[1]
                # if we the distance to a node v from the current node is 
                # less than the current distance recorded for the node, update its distance
                if dist[v] > dist[u] + w:  
                    dist[v] = dist[u] + w
                    pred[v] = u
                    heapq.heappush(q, (dist[v],v))
    return dist, pred
