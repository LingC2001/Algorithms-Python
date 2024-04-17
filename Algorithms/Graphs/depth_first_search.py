"""
DFS complexity analysis

Each vertex is visited once, and all the outgoing edges of the vertex are checked.

Time Complexity:
    Using an adjacency list: O(V + E) for directed and O(V + 2E) for undirected graphs
    Using an adjacency matrix: O(V^2), since V columns are checked for each Vertex.

Space complexity
    In worst case the graph is a striaght line, therefore:
    Worst case aux space: O(V), not counting adj_matrix or adj_list used
    Also because of the visited and res arrays created
""" 


def depth_first_search(adj_list):

    n = len(adj_list)
    visited = [False]*n
    res = []

    for i in range(n):
        if not visited[i]:
            dfs(adj_list, i, visited, res)

    return res

def dfs(adj_list, vertex, visited, res):
        visited[vertex] = True
        res.append(vertex)
        
        for e in adj_list[vertex]:
            if not visited[e]:
                dfs(adj_list, e, visited, res)