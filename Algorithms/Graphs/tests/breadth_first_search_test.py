import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from breadth_first_search import breadth_first_search
import pytest

def test_empty():
    adj_matrix = []
    res = breadth_first_search(adj_matrix, None)
    assert res == []

def test_1():
    # vertex 0 is connected to all other vetices
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    res = breadth_first_search(adj_matrix, 0)
    assert res == [0, 1, 2, 3, 4]

def test_2():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0]]
    res = breadth_first_search(adj_matrix, 0)
    assert res == [0, 1, 2, 3]

def test_3():
    adj_matrix = [[0, 1, 0, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    res = breadth_first_search(adj_matrix, 0)
    assert res == [0, 1, 3, 4]

def test_4():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    res = breadth_first_search(adj_matrix, 0)
    assert res == [0, 1, 2]

def test_5():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    res = breadth_first_search(adj_matrix, 0)
    assert res == [0, 1, 2]

def test_6():
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    res = breadth_first_search(adj_matrix, 3)
    assert res == [3, 0, 1, 2, 4]