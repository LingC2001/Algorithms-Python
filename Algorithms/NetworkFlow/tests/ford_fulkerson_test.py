import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from ford_fulkerson import ford_fulkerson
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

    assert ford_fulkerson(G, 0, 7)[0] == 2
    
    # below are technically invalid tests because sources must have indegree of 0
    # and sinks must have outdegree of 0
    assert ford_fulkerson(G, 4, 7)[0] == 8 
    assert ford_fulkerson(G, 5, 4)[0] == 0
    assert ford_fulkerson(G, 2, 7)[0] == 1

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

    assert ford_fulkerson(G, 0, 5)[0] == 5

    # technically invalid tests
    assert ford_fulkerson(G, 2, 5)[0] == 2
    assert ford_fulkerson(G, 4, 5)[0] == 6
    assert ford_fulkerson(G, 1, 5)[0] == 2
    assert ford_fulkerson(G, 3, 5)[0] == 5

    assert ford_fulkerson(G, 0, 2)[0] == 11
    assert ford_fulkerson(G, 1, 0)[0] == 0

# AI tests

def test_ford_fulkerson():
    adj_list = [
        [(1, 2), (2, 3)],
        [(2, 1), (3, 1)],
        [(3, 2)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 3

def test_ford_fulkerson_no_path():
    adj_list = [
        [(1, 2)],
        [(2, 1)],
        [],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 0

def test_ford_fulkerson_multiple_paths():
    adj_list = [
        [(1, 2), (2, 2)],
        [(2, 1), (3, 1)],
        [(3, 2)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 3

def test_ford_fulkerson_back_edge():
    adj_list = [
        [(1, 2)],
        [(0, 1), (2, 1)],
        [(3, 2)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 1

def test_ford_fulkerson_self_loop():
    adj_list = [
        [(0, 2), (1, 2)],
        [(2, 1)],
        [(3, 2)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 1

def test_ford_fulkerson_multiple_paths1():
    adj_list = [
        [(1, 3), (2, 2)],
        [(3, 3)],
        [(3, 2)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 5

def test_ford_fulkerson_self_loop1():
    adj_list = [
        [(1, 2), (0, 100)],
        [(2, 2)],
        [(3, 2)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 2

def test_ford_fulkerson_multiple_paths2():
    adj_list = [
        [(1, 2), (2, 3)],
        [(2, 1), (3, 2)],
        [(3, 3)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 5

def test_ford_fulkerson_self_loop2():
    adj_list = [
        [(1, 2)],
        [(1, 1), (2, 3)],
        [(3, 2)],
        []
    ]
    max_flow, _ = ford_fulkerson(adj_list, 0, 3)
    assert max_flow == 2