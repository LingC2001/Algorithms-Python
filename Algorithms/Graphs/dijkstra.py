import heapq
import math
def dijkstra(G, s):
    """
    performs dijkstra's algorithm on a weighted graph G
    G is represented as a weighted adjacency matrix
        - the 
    s is the source
    
    """
    dist = [math.inf] * len(G)
    pred = [-1] * len(G)
    dist[s] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (s, 0))

    while q:
        u, key = heapq.heappop(q)
        if dist[u] == key:
            for v in range(len(G[u])):
                if G[u][v] != 0:
                    if dist[v] > dist[u] + G[u][v]:
                        dist[v] = dist[u] + G[u][v]
                        pred[v] = u
                        heapq.heappush(q, (v, dist[v]))
    return dist, pred