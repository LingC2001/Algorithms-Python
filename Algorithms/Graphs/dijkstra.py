import heapq
import math
def dijkstra(G, s):
    """
    performs dijkstra's algorithm on a weighted graph G
    G is represented as a weighted adjacency matrix
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
            for v in range(len(G[u])):
                if G[u][v] != 0: # for all the edges coming out from the node
                    # update the costs/dists using triangle inequality

                    # if we the distance to a node v from the current node is 
                    # less than the current distance recorded for the node, update its distance
                    if dist[v] > dist[u] + G[u][v]:  
                        dist[v] = dist[u] + G[u][v]
                        pred[v] = u
                        heapq.heappush(q, (dist[v],v))
    return dist, pred
