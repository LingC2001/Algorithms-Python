
def topological_sort_dfs(adj_matrix):
    
    def dfs(u):
        visited[u] = True
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1 and not visited[v]:
                dfs(v)
        order.append(u)

    
    n = len(adj_matrix)
    order = []
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(i)

    order.reverse()
    return order

