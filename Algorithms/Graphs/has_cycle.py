"""
Has Cycle complexity analysis:

We just perform dfs until an edge leads to an already visited node that is not where we just came from. 
Therefore has the same complexity as dfs.

Time Complexity:
    Using an adjacency list: O(V + E) for directed and O(V + 2E) for undirected graphs
    Using an adjacency matrix: O(V^2), since V columns are checked for each Vertex.

Space complexity
    In worst case the graph is a striaght line, therefore:
    Worst case aux space: O(V), not counting adj_matrix or adj_list used

"""

def has_cycle(adj_list):
    """
    During dfs traversal (of undirected graphs), 
    if we encounter a vertex that has already been visited before,
    that is also not the vertex that we just came from,
    then a cycle exists
    
    """
    

    n = len(adj_list)
    visited = [False]*n

    for i in range(n):
        if not visited[i]:
            if dfs(adj_list, i, None, visited):
                return True
    return False

def dfs(adj_list, vertex, parent, visited):
        visited[vertex] = True
        
        for e in adj_list[vertex]:
            if visited[e] and e != parent:
                return True
            elif not visited[e]:
                if dfs(adj_list, e, vertex, visited):
                    return True