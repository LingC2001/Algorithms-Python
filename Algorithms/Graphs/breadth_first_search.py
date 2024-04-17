"""
BFS complexity analysis:

Like DFS, BFS also visits everyone node once,
and checks all the edges once for directed graphs,
and checks all the edges twice for undirected graphs

BFS is implemented iteratively with a queue,
whereas DFS can be implemented recursively or iteratively with a stack

Time Complexity:
    Using an adjacency list: O(V + E) for directed and O(V + 2E) for undirected graphs
    Using an adjacency matrix: O(V^2), since V columns are checked for each Vertex.

Space Complexity:
    The maximum size of the queue can be at one time is O(V)

"""


from collections import deque
def breadth_first_search(adj_list, s):
    """
    perfroms bfs of a graph given adjacency matrix and a starting node index
    """
    if s is None:
        return []
    n = len(adj_list)
    visited = [False]*n
    visited[s] = True
    q = deque([s])
    res = [s]

    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True 
                q.append(v)
                res.append(v)
    
    return res


