import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from connected_components import connected_components
import pytest

def test_empty():
    adj_matrix = []
    adj_list = []
    res = connected_components(adj_list)
    assert res == (0, [])

def test_1():
    # vertex 0 is connected to all other vetices
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    adj_list = [[1, 2, 3, 4],
                [0],
                [0],
                [0],
                [0]]
    res = connected_components(adj_list)
    assert res == (1, [1, 1, 1, 1, 1])

def test_2():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0]]
    adj_list = [[1, 2],
                [0, 3],
                [0, 3],
                [1, 2],
                []]
    res = connected_components(adj_list)
    assert res == (2, [1, 1, 1, 1, 2])

def test_3():
    adj_matrix = [[0, 1, 0, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    adj_list = [[1],
                [0, 3],
                [],
                [1, 4],
                [3]]
    res = connected_components(adj_list)
    assert res == (2, [1, 1, 2, 1, 1])

def test_4():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    adj_list = [[1,2],
                [0],
                [0],
                [4],
                [3]]
    res = connected_components(adj_list)
    assert res == (2, [1, 1, 1, 2, 2])