from collections import deque

def breadth_first_search(adj_matrix, s):
    """
    perfroms bfs of a graph given adjacency matrix and a starting node index
    """
    if s is None:
        return []
    n = len(adj_matrix)
    visited = [False]*n
    visited[s] = True
    q = deque([s])
    res = [s]

    while q:
        u = q.popleft()
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1:
                if not visited[v]:
                    visited[v] = True 
                    q.append(v)
                    res.append(v)
    
    return res


