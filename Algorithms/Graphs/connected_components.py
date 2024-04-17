"""
Connected components complexity analysis:

We just perofrm dfs until all nodes are visited. Therefore has the same complexity as dfs.

Time Complexity:
    Using an adjacency list: O(V + E) for directed and O(V + 2E) for undirected graphs
    Using an adjacency matrix: O(V^2), since V columns are checked for each Vertex.

Space complexity
    In worst case the graph is a striaght line, therefore:
    Worst case aux space: O(V), not counting adj_matrix or adj_list used
    Also because of the components arary of size V created
"""

def connected_components(adj_list):
    """
    Notice how each starting dfs call visits exactly one connected component.
    Therefore the number of connected components is just the number of dfs we need to perform
    before all nodes are visited (not counting recursive calls)

    Instead of keeping a visited list, and having a separate components list, we will combine them
    and just have a components list that has initial values of None
    """

    n = len(adj_list)
    components = [None]*n
    component_num = 0

    for i in range(n):
        if components[i] is None:
            component_num += 1
            dfs(adj_list, i, components, component_num)

    return component_num, components

def dfs(adj_list, vertex, components, component_num):
        components[vertex] = component_num
        
        for e in adj_list[vertex]:
            if components[e] is None:
                dfs(adj_list, e, components, component_num)