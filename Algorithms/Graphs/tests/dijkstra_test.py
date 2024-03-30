import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from dijkstra import dijkstra
import pytest


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
    s = 0

    dist, pred = dijkstra(G, s)
    assert dist == [0, 2, 8, 9, 10, 9, 12, 14]
    assert pred == [-1, 0, 1, 2, 3, 2, 5, 6]

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
    pred = [1, 2, -1, 2 , 3, 2, 5, 6]

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

    dist, pred = dijkstra(G, s)
    assert dist == [8, 6, 0, 1, 2, 1, 4, 6]
    assert pred == [1, 2, -1, 2 , 3, 2, 5, 6]


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
    pred = [0, 2, 3, 0, 3, 2, 5, 6]

    """
    G = [[0, 0, 0, 10, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, 0, 0, 0],
         [0, 6, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 6, 0, 6],
         [0, 0, 0, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0]]
    s = 0

    dist, pred = dijkstra(G, s)
    assert dist == [0, 17, 11, 10, 11, 12, 15, 17]
    assert pred == [-1, 2, 3, 0, 3, 2, 5, 4]