import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from prim_mst import prim_mst
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
    s = 0
    dist, parent = prim_mst(G, s)
    assert dist == [0, 2, 1]
    assert parent == [None, 0, 1]


def test_undirected_1():
    """

    v0 -- 10 -- v3 -- 1 -- v4 -- 6 -- v7
    |           |          |           |
    2           1          6           2
    |           |          |           |
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
    s = 0

    dist, parent = prim_mst(G, s)
    assert dist == [0, 2, 6, 1, 1, 1, 3, 2]
    assert parent == [None, 0, 1, 2, 3, 2, 5, 6]

def test_undirected_2():
    """

    v0 -- 10 -- v3 -- 1 -- v4 -- 6 -- v7
    |           |          |           |
    2           1          6           2
    |           |          |           |
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
    s = 2

    dist, parent = prim_mst(G, s)
    assert dist == [2, 6, 0, 1, 1, 1, 3, 2]
    assert parent == [1, 2, None, 2 , 3, 2, 5, 6]

