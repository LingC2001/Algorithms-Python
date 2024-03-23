import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from shortest_paths import shortest_paths
import pytest

def test_empty():
    adj_matrix = []
    res = shortest_paths(adj_matrix, None, [])
    assert res == []

def test_empty_search():
    # vertex 0 is connected to all other vetices
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    res = shortest_paths(adj_matrix, 0, [])
    assert res == []

def test_1():
    # vertex 0 is connected to all other vetices
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    res = shortest_paths(adj_matrix, 0, [4])
    assert res == [[0, 4]]

def test_2():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0]]
    res = shortest_paths(adj_matrix, 0, [2])
    assert res == [[0, 2]]

def test_no_path():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0]]
    res = shortest_paths(adj_matrix, 0, [4])
    assert res == [[]]

def test_multi_search():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0]]
    res = shortest_paths(adj_matrix, 0, [2,3,4])
    assert res == [[0, 2], [0, 1, 3], []]

def test_3():
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    res = shortest_paths(adj_matrix, 3, [1, 4])
    assert res == [ [3, 0, 1] ,[3, 0, 4]]