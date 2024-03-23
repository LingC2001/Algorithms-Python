

def connected_components(adj_matrix):
    """
    Notice how each starting dfs call visits exactly one connected component.
    Therefore the number of connected components is just the number of dfs we need to perform
    before all nodes are visited (not counting recursive calls)

    Instead of keeping a visited list, and having a separate components list, we will combine them
    and just have a components list that has initial values of None
    """
    def dfs(vertex):
        components[vertex] = num_components
        
        for i in range(len(adj_matrix[vertex])):
            if adj_matrix[vertex][i] == 1 and components[i] is None:
                dfs(i)

    n = len(adj_matrix)
    components = [None]*n
    num_components = 0

    for i in range(n):
        if components[i] is None:
            num_components += 1
            dfs(i)

    return num_components, components