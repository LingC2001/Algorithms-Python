from collections import deque

def topological_sort_khan(adj_matrix):
    """
    given a directed acyclic graph
    """
    order = []
    ready = deque()
    in_degree = calculate_in_degree(adj_matrix)
    # add all vertices with no incoming edges
    
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            ready.append(i)


    while ready:
        u = ready.popleft()
        order.append(u)
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1:
                # remove edge (don't need to actually delete it if using in degree method)
                in_degree[v] -= 1

                if in_degree[v] == 0:    
                    ready.append(v)
                    
    return order

def calculate_in_degree(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n

    for u in range(n):
        for v in range(n):
            if adj_matrix[u][v] == 1:
                in_degree[v] += 1
    return in_degree
