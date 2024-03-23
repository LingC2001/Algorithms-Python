
def has_cycle(adj_matrix):
    """
    During dfs traversal (of undirected graphs), 
    if we encounter a vertex that has already been visited before,
    that is also not the vertex that we just came from,
    then a cycle exists
    
    """
    def dfs(vertex, parent):
        visited[vertex] = True
        
        for i in range(len(adj_matrix[vertex])):
            if adj_matrix[vertex][i] == 1:
                if visited[i] and i != parent:
                    return True
                elif not visited[i]:
                    if dfs(i, vertex):
                        return True

    n = len(adj_matrix)
    visited = [False]*n

    for i in range(n):
        if not visited[i]:
            if dfs(i, None):
                return True
    return False

