
def dfs_traverse(adj_matrix):

    def dfs(vertex):
        visited[vertex] = True
        res.append(vertex)
        
        for i in range(len(adj_matrix[vertex])):
            if adj_matrix[vertex][i] == 1 and not visited[i]:
                dfs(i)

    n = len(adj_matrix)
    visited = [False]*n
    res = []

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return res