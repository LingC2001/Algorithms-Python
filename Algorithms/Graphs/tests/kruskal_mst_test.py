import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from kruskal_mst import kruskal_mst
import pytest

def test_triangle():
    """
    
    v0 --2-- v1
    |      /
    2     /
    |    1
    |   /
    |  /
    v2
    
    The shortest path would give v0-> v1 = 2, v0 -> v2 = 2
        - having a total edge weight of 4, but minimised path to v1 and v2
    
    Whereas the minimum spanning tree would be: v0 -> v1 -> v2 or v0 -> v2 -> v1 
        - both having a edge weight of 3
    """
    G = [[0, 2, 2],
         [2, 0, 1],
         [2, 1, 0]]
    
    # creating adj list:
    G_list = [[] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                G_list[i].append((j, G[i][j]))
    G = G_list

    T = kruskal_mst(G)
    assert T == [[0, 2, 0],
                [2, 0, 1],
                [0, 1, 0]] or T == [[0, 0, 2],
                                    [0, 0, 1],
                                    [2, 1, 0]]


def test_undirected():
    """

    v0 -- 10 -- v3 -- 1 -- v4 -- 6 -- v7
    |           |          |           |
    2           1          6           2
    |           |          |           |
    v1 -- 6 --- v2 -- 1 -- v5 -- 3 -- v6

    should become mst:

    v0          v3 -- 1 -- v4          v7
    |           |                      |
    2           1                      2
    |           |                      |
    v1 -- 6 --- v2 -- 1 -- v5 -- 3 -- v6

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


    T = kruskal_mst(G)
    assert T == [[0, 2, 0, 0, 0, 0, 0, 0],
                 [2, 0, 6, 0, 0, 0, 0, 0],
                 [0, 6, 0, 1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 3, 0],
                 [0, 0, 0, 0, 0, 3, 0, 2],
                 [0, 0, 0, 0, 0, 0, 2, 0]]

