"""
Shortest Paths (from source) complexity analysis:

BFS can be used to solve this problem given an unweighted graph, or if all weights are equal.

Time Complexity:
    The DFS part:
    Using an adjacency list: O(V + E) for directed and O(V + 2E) for undirected graphs
    Using an adjacency matrix: O(V^2), since V columns are checked for each Vertex.

    The get_path part:
    Worst case: O(V) path length for V nodes = O(V^2), if we extract the path for every node
                - if only one destination node specified, then O(V)
    
    Combined: O(V^2)

Space Complexity:
    The maximum size of the queue can be at one time is O(V)
    Also visited is O(V)
    Paths can be O(v^2) worst case
"""

from collections import deque

def shortest_paths(adj_list, s, vertices):
    """
    finds the shortest paths from s to all vertices specified in :param: vertices
    """
    dist, pred = bfs(adj_list, s)
    paths = []

    for v in vertices:
        if dist[v] != -1: # path was found
            paths.append(get_path(s, v, pred))
        else:
            paths.append([])

    return paths



def bfs(adj_list, s):
    """
    perfroms bfs of a graph given adjacency list and a starting node index
    """
    if s is None:
        return [], []
    
    n = len(adj_list)
    dist = [-1]*n #replaces visited and keeps track of distance from s
    dist[s] = 0
    pred = [None]*n # the predecessor of each node, keeps track of the path we came from
    q = deque([s])

    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                pred[v] = u
                q.append(v)
    
    return dist, pred

def get_path(s, u, pred):
    path = [u]
    while u != s:
        path.append(pred[u])
        u = pred[u]
    path.reverse()
    return path
