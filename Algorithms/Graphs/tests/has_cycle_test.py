import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from has_cycle import has_cycle
import pytest

def test_empty():
    adj_matrix = []
    res = has_cycle(adj_matrix)
    assert res == False

def test_1():
    # vertex 0 is connected to all other vetices
    adj_matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0]]
    res = has_cycle(adj_matrix)
    assert res == False
def test_2():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0]]
    res = has_cycle(adj_matrix)
    assert res == True

def test_3():
    adj_matrix = [[0, 1, 0, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    res = has_cycle(adj_matrix)
    assert res == False

def test_4():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    res = has_cycle(adj_matrix)
    assert res == False

def test_5():
    adj_matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0]]
    res = has_cycle(adj_matrix)
    assert res == True