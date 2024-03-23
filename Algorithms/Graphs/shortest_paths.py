from collections import deque

def shortest_paths(adj_matrix, s, vertices):
    """
    finds the shortest paths from s to all vertices specified in :param: vertices
    """
    dist, pred = bfs(adj_matrix, s)
    paths = []

    for v in vertices:
        if dist[v] != -1: # path was found
            paths.append(get_path(s, v, pred))
        else:
            paths.append([])

    return paths



def bfs(adj_matrix, s):
    """
    perfroms bfs of a graph given adjacency matrix and a starting node index
    """
    if s is None:
        return [], []
    
    n = len(adj_matrix)
    dist = [-1]*n #replaces visited and keeps track of distance from s
    dist[s] = 0
    pred = [None]*n # the predecessor of each node, keeps track of the path we came from
    q = deque([s])

    while q:
        u = q.popleft()
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1:
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
