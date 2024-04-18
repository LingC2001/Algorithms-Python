"""
Kruskal's Algorithm complexity analysis:

Time complexity:
    All the edges are first sorted, O(Elog(E))
        This is why edge list representation would work best for this algorithm.
        Otherwise we would need to extract the edges and put them in one list,
        which is O(E) for adj_list and O(V^2) for adj_matrix

    For each edge, UnionFind operations are performed, 
        without optimisation, it would be O(log(V)) for each operation, so O(ELog(V))
        with both path compression and union by rank, it would be approx O(1) for each operation, so O(E)
    
    In total, it is just O(ELog(E)), and for simple graphs, since O(Log(E)) = O(Log(V^2)) = O(2Log(V))
    it is O(ELog(V))

Space complexity:
    O(V^2) for the adjacency matrix of the new Tree
        if it was adj_list instead, would be O(V + E)
    O(E) for the edge list
"""


from union_find import UnionFind

def kruskal_mst(G):
    """
    Kruskal's algorithm for finding minimum spanning trees using
    Union Find Disjoint Set data structure for quickly determining whether
    the selected edge will create a cycle or not.

    Kruskal's algorithm uses Greedy approach and selects the minimum
    weighted edge in the entire graph every iteration, that does not create a cycle.
    Since it doesn't have to start at a specific node, it can actually find multiple
    disconnected MSTs.

    """
    n = len(G)
    # create an empty graph to represent our Tree
    T = []
    for i in range(n):
        T.append([0]*n)
    
    # extract all edges from graph
    E = []
    for u in range(len(G)):
        for e in G[u]:
            E.append((e[1], (u, e[0])))

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
    

