from union_find import UnionFind

def kruskal_mst(G):
    """
    Kruskal's algorithm for finding minimum spanning trees using
    Union Find Disjoint Set data structure for quickly determining whether
    the selected edge will create a cycle or not.

    Kruskal's algorithm uses Greedy approach and selects the minimum
    weighted edge in the entire graph every iteration.

    """
    n = len(G)
    # create an empty graph to represent our Tree
    T = []
    for i in range(n):
        T.append([0]*n)
    
    # extract all edges from graph
    E = []
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                E.append((G[u][v], (u, v)))

    # sort edges for minimum weight
    E.sort(key= lambda x: x[0])
    
    # initialise union find disjoint set data structure to help determine whether an
    # edge connects 2 disjoint sets, or if it will create a cycle (connecting already connected set together )
    forest = UnionFind(n)

    for e in E:
        w = e[0]
        u = e[1][0]
        v = e[1][1]
        if forest.find(u) != forest.find(v): # if 2 disjoint sets
            forest.union(u, v)
            T[u][v] = w
            T[v][u] = w
    
    return T
    

