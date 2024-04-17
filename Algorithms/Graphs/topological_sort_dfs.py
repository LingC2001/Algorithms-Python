"""
DFS for topological sorting:

The idea is that during post-order traversal DFS, a parent node v will only be
visited/processed after all the children/dependents are visited. 
Therefore we will just insert the elements in post-order traversal order and 
then reverse it at the end to get topological order.

Time complexity:
    adj_list: O(V+E) for dfs, O(V) for reversing
    adj_matrix: O(V^2) for dfs, O(V) for reversing

Space complexity:
    O(n), for order list and visited list, and dfs recursion stack

"""


def topological_sort_dfs(adj_list):

    n = len(adj_list)
    order = []
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(adj_list, i, visited, order)

    order.reverse()
    return order

def dfs(adj_list, u, visited, order):
    visited[u] = True
    for v in adj_list[u]:
        if not visited[v]:
            dfs(adj_list, v, visited, order)
    order.append(u)