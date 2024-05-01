import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from critical_path import critical_path
import pytest


def test_dag():
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

    Using above graph,
    where s = v0
    then 
    dist = [0, 17, 11, 10, 11, 12, 15, 17]
    pred = [None, 2, 3, 0, 3, 2, 5, 6]

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

    longest = critical_path(G)

    assert longest == 22


def test_negative_edges_no_cycle():
    """
    kind of a weird test
    most applications won't have negative edges.
    """
    adj_list = [
        [(1, 1), (2, 1)],
        [(3, -5)],
        [(4, -6)],
        [(5, 2)],
        [],
        [],
    ]
    
    longest = critical_path(adj_list)
    assert longest == 2