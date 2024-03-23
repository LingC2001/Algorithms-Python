import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from depth_first_search import dfs_traverse
import pytest

def test_empty():
    adj_matrix = []
    res = dfs_traverse(adj_matrix)
    assert res == []

def test_1():
    # vertex 0 is connected to all other vetices
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    res = dfs_traverse(adj_matrix)
    assert res == [0, 1, 2, 3, 4]

def test_2():
    # vertex 0 is connected to 1, which is connected to 3, which is connected to 2
    # vertex 4 is not connected to anything but is still traversed since the algorithm
    # is designed to traverse all nodes even if they are not connected
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0]]
    res = dfs_traverse(adj_matrix)
    assert res == [0, 1, 3, 2, 4]

def test_3():
    adj_matrix = [[0, 1, 0, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    res = dfs_traverse(adj_matrix)
    assert res == [0, 1, 3, 4, 2]