import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from minimum_cut import minimum_cut
import pytest


def test_1():
    """
    All tests will be done on:
    G =

    v0 -- 10 --> v3 -- 1 --> v4 -- 6 --> v7
                |          |           ^
                |          |           |
                1          6           2
                |          |           |
                V          V           |
    v1 <-- 6 --- v2 -- 1 --> v5 -- 3 --> v6

    """
    G = [[0, 0, 0, 10, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
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

    assert minimum_cut(G, 0, 7) == (2, {3, 0}, {1, 2, 4, 5, 6, 7}) \
        or minimum_cut(G, 0, 7) == (2, {0, 1, 2, 3}, {4, 5, 6, 7})

    assert minimum_cut(G, 0, 1) == (1, {0, 3, 4, 5, 6, 7}, {2, 1} )

def test_2():
    G = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]
    
    # creating adj list:
    G_list = [[] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                G_list[i].append((j, G[i][j]))
    G = G_list

    assert minimum_cut(G, 0, 5) == (5, {0, 1, 2}, {3, 4, 5}) 
