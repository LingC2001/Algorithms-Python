import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from floyd_warshall import floyd_warshall
from floyd_warshall import get_path
import pytest
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

    dist, succ = floyd_warshall(G)
    assert dist[0][3] == 9 and get_path(dist, succ, 0, 3) == [0, 1, 2, 3]
    assert dist[0][5] == 9 and get_path(dist, succ, 0, 5) == [0, 1, 2, 5]
    assert dist[3][4] == 1 and get_path(dist, succ, 3, 4) == [3, 4]
    assert dist[4][6] == 6 and get_path(dist, succ, 4, 6) == [4, 3, 2, 5, 6]


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

    dist, succ = floyd_warshall(G)
    
    assert get_path(dist, succ, 0, 3) == [0, 3]
    assert get_path(dist, succ, 0, 4) == [0, 3, 4]
    assert get_path(dist, succ, 0, 2) == [0, 3, 2]
    assert get_path(dist, succ, 0, 1) == [0, 3, 2, 1]
    assert get_path(dist, succ, 0, 7) == [0, 3, 4, 7]
    assert get_path(dist, succ, 0, 6) == [0, 3, 2, 5, 6]
    assert get_path(dist, succ, 0, 0) == [0]

def test_negative_cycle_simple():
    adj_list = [
        [(1, 2)],
        [(0, -3), (2, 1)],
        [(1, 1)],
        [(2, 1)]
    ]
    dist, succ = floyd_warshall(adj_list)

    assert dist[0][0] == -inf and get_path(dist, succ, 0, 0) == -1
    assert dist[0][1] == -inf and get_path(dist, succ, 0, 1) == -1
    assert dist[1][0] == -inf and get_path(dist, succ, 1, 0) == -1
    assert dist[0][2] == -inf and get_path(dist, succ, 0, 2) == -1
    assert dist[2][2] == -inf and get_path(dist, succ, 2, 2) == -1
    assert dist[2][0] == -inf and get_path(dist, succ, 2, 0) == -1
    assert dist[0][3] == inf and get_path(dist, succ, 0, 3) == None
    assert dist[3][0] == -inf and get_path(dist, succ, 3, 0) == -1
    assert dist[3][2] == -inf and get_path(dist, succ, 3, 2) == -1
    assert dist[3][3] == 0 and get_path(dist, succ, 3, 3) == [3]


def test_negative_cycle():

    adj_list = [
        [(1, 5)],
        [(2, 1), (3, 2)],
        [(4, 1)],
        [(5, 2)],
        [(3, -1)],
        [(4, -3)]
    ]
    
    dist, succ = floyd_warshall(adj_list)

    assert dist[0][1] == 5 and get_path(dist, succ, 0, 1) == [0, 1]
    assert dist[0][2] == 6 and get_path(dist, succ, 0, 2) == [0, 1, 2]
    assert dist[1][2] == 1 and get_path(dist, succ, 1, 2) == [1, 2]
    assert dist[2][1] == inf and get_path(dist, succ, 2, 1) == None
    assert dist[0][4] == -inf and get_path(dist, succ, 0, 4) == -1
    assert dist[4][3] == -inf and get_path(dist, succ, 4, 3) == -1
    assert dist[4][5] == -inf and get_path(dist, succ, 4, 5) == -1


def test_negative_edges_no_cycle():
    adj_list = [
        [(1, 1), (2, 1)],
        [(3, -5)],
        [(4, -6)],
        [(5, 2)],
        [],
        [],
    ]
    
    dist, succ = floyd_warshall(adj_list)
    
    assert dist[0][5] == -2 and get_path(dist, succ, 0, 5) == [0, 1, 3, 5]
    assert dist[3][5] == 2 and get_path(dist, succ, 3, 5) == [3, 5]
    assert dist[5][3] == inf and get_path(dist, succ, 5, 3) == None
    assert dist[0][4] == -5 and get_path(dist, succ, 0, 4) == [0, 2, 4]


    adj_list = [
        [(1, 1), (2, 1)],
        [(3, -5)],
        [(4, -6)],
        [(5, 2)],
        [(5, 1)],
        [],
    ]
    
    dist, succ = floyd_warshall(adj_list)


def test_negative_edges_no_negative_cycle():
    adj_list = [
        [(1, -3)],
        [(2, -2)],
        [(3, 3)],
        [(0, 3)]
    ]

    dist, succ = floyd_warshall(adj_list)
    assert dist[0][3] == -2 and get_path(dist, succ, 0, 3) == [0, 1, 2, 3]
    assert dist[0][2] == -5 and get_path(dist, succ, 0, 2) == [0, 1, 2]
    assert dist[3][2] == -2 and get_path(dist, succ, 3, 2) == [3, 0, 1, 2]

    adj_list = [
        [(1, -3)],
        [(2, -2)],
        [(3, 3)],
        [(1, -1)]
    ]

    dist, succ = floyd_warshall(adj_list)
    assert dist[0][3] == -2 and get_path(dist, succ, 0, 3) == [0, 1, 2, 3]
    assert dist[0][2] == -5 and get_path(dist, succ, 0, 2) == [0, 1, 2]
    assert dist[0][1] == -3 and get_path(dist, succ, 0, 1) == [0, 1]
    assert dist[1][2] == -2 and get_path(dist, succ, 1, 2) == [1, 2]
    assert dist[3][1] == -1 and get_path(dist, succ, 3, 1) == [3, 1]
    assert dist[2][0] == inf and get_path(dist, succ, 2, 0) == None

    # with negative cycle

    adj_list = [
        [(1, -3)],
        [(2, -2)],
        [(3, 3)],
        [(1, -2)]
    ]

    dist, succ = floyd_warshall(adj_list)

    assert dist[0][3] == -inf and get_path(dist, succ, 0, 3) == -1
    assert dist[0][2] == -inf and get_path(dist, succ, 0, 2) == -1
    assert dist[0][1] == -inf and get_path(dist, succ, 0, 1) == -1
    assert dist[1][2] == -inf and get_path(dist, succ, 1, 2) == -1
    assert dist[3][1] == -inf and get_path(dist, succ, 3, 1) == -1
    assert dist[2][0] == inf and get_path(dist, succ, 2, 0) == None
