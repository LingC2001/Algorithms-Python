import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from transitive_closure import transitive_closure

inf = float('inf')

def test_undirected():
    """
    All tests will be done on:
    G =

    v0 -- 10 -- v3 -- 1 -- v4 -- 6 -- v7
    |           |          |           |
    2           1          6           2
    |           |          |           |
    v1 -- 6 --- v2 -- 1 -- v5 -- 3 -- v6

    Using above graph,
    where s = v0,
    then dist = [0, 2, 8, 9, 10, 9, 12, 14]

    """
    G = [[0, 2, 0, 10, 0, 0, 0, 0],
         [2, 0, 6, 0, 0, 0, 0, 0],
         [0, 6, 0, 1, 0, 1, 0, 0],
         [10, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 6, 0, 6],
         [0, 0, 1, 0, 6, 0, 3, 0],
         [0, 0, 0, 0, 0, 3, 0, 2],
         [0, 0, 0, 0, 6, 0, 3, 0]]
    
    # creating adj list:
    G_list = [[] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                G_list[i].append((j, G[i][j]))
    G = G_list

    connected = transitive_closure(G)
    assert connected == [[True]*len(G) for i in range(len(G))]


def test_directed():
    """
    All tests will be done on:
    G =

    v0 -- 10 --> v3 -- 1 --> v4 -- 6 --> v7
    ^           |          |           ^
    |           |          |           |
    2           1          6           2
    |           |          |           |
    |           V          V           |
    v1 <-- 6 --- v2 -- 1 --> v5 -- 3 --> v6

    Using above graph,
    where s = v0
    then 
    dist = [0, 17, 11, 10, 11, 12, 15, 17]
    pred = [None, 2, 3, 0, 3, 2, 5, 6]

    """
    G = [[0, 0, 0, 10, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, 0, 0, 0],
         [0, 6, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 6, 0, 6],
         [0, 0, 0, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0]]
    
    # creating adj list:
    G_list = [[] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                G_list[i].append((j, G[i][j]))
    G = G_list

    connected = transitive_closure(G)
    t = True
    f = False
    assert connected == [
        [t, t, t, t, t, t, t, t],
        [t, t, t, t, t, t, t, t],
        [t, t, t, t, t, t, t, t],
        [t, t, t, t, t, t, t, t],
        [f, f, f, f, t, t, t, t],
        [f, f, f, f, f, t, t, t],
        [f, f, f, f, f, f, t, t],
        [f, f, f, f, f, f, f, t]
    ]