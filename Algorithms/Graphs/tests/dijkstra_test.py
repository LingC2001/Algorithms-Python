import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from dijkstra import dijkstra
import pytest
import math

def get_path(s, u, pred):
    path = [u]
    while u != s:
        path.append(pred[u])
        u = pred[u]
    path.reverse()
    return path

def test_undirected_1():
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

    s = 0

    dist, pred = dijkstra(G, s)
    assert dist == [0, 2, 8, 9, 10, 9, 12, 14]
    assert pred == [None, 0, 1, 2, 3, 2, 5, 6]

def test_undirected_2():
    """
    All tests will be done on:
    G =

    v0 -- 10 -- v3 -- 1 -- v4 -- 6 -- v7
    |           |          |           |
    2           1          6           2
    |           |          |           |
    v1 -- 6 --- v2 -- 1 -- v5 -- 3 -- v6

    Using above graph,
    where s = v2,
    then 
    dist = [8, 6, 0, 1, 2, 1, 4, 6]
    pred = [1, 2, None, 2 , 3, 2, 5, 6]

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
    s = 2

    dist, pred = dijkstra(G, s)
    assert dist == [8, 6, 0, 1, 2, 1, 4, 6]
    assert pred == [1, 2, None, 2 , 3, 2, 5, 6]


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
    s = 0

    dist, pred = dijkstra(G, s)
    assert dist == [0, 17, 11, 10, 11, 12, 15, 17]
    assert pred == [None, 2, 3, 0, 3, 2, 5, 4]

def test_paths():
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
    s = 0

    dist, pred = dijkstra(G, s)
    
    assert get_path(s, 3, pred) == [0, 3]
    assert get_path(s, 4, pred) == [0, 3, 4]
    assert get_path(s, 2, pred) == [0, 3, 2]
    assert get_path(s, 1, pred) == [0, 3, 2, 1]
    assert get_path(s, 7, pred) == [0, 3, 4, 7]
    assert get_path(s, 6, pred) == [0, 3, 2, 5, 6]
    assert get_path(s, s, pred) == [0]


# ai tests:
def test_dijkstra_simple():
    G = [[(1, 1), (2, 5)], [(2, 2)], []]
    dist, pred = dijkstra(G, 0)
    assert dist == [0, 1, 3]
    assert pred == [None, 0, 1]


def test_dijkstra_disconnected_graph():
    G = [[(1, 1)], [], []]
    dist, pred = dijkstra(G, 0)
    assert dist == [0, 1, math.inf]
    assert pred == [None, 0, None]

def test_dijkstra_two_nodes():
    G = [[(1, 1)], []]
    dist, pred = dijkstra(G, 0)
    assert dist == [0, 1]
    assert pred == [None, 0]

def test_dijkstra_one_node():
    G = [[]]
    dist, pred = dijkstra(G, 0)
    assert dist == [0]
    assert pred == [None]

def test_dijkstra_invalid_source():
    G = [[(1, 1)], []]
    with pytest.raises(IndexError):
        dijkstra(G, 2)


def test_dijkstra_b():
    # Test case 1: Simple graph
    G = [[(1, 2), (2, 3)], [(0, 2), (2, 1)], [(0, 3), (1, 1)]]
    dist, pred = dijkstra(G, 0)
    assert dist == [0, 2, 3]
    assert pred == [None, 0, 0]


    # Test case 3: Disconnected graph
    G = [[(1, 2)], [], [(0, 3)]]
    dist, pred = dijkstra(G, 0)
    assert dist == [0, 2, math.inf]
    assert pred == [None, 0, None]

    # Test case 4: Graph with zero-weight edges
    G = [[(1, 0), (2, 3)], [(0, 0), (2, 1)], [(0, 3), (1, 1)]]
    dist, pred = dijkstra(G, 0)
    assert dist == [0, 0, 1]
    assert pred == [None, 0, 1]

    # Test case 5: Single-node graph
    G = [[]]
    dist, pred = dijkstra(G, 0)
    assert dist == [0]
    assert pred == [None]