import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from topological_sort_khan import topological_sort_khan
import pytest

def test_empty():
    adj_matrix = []
    res = topological_sort_khan(adj_matrix)
    assert res == []

def test_line_graph():
    """
    3 -> 0 -> 1 -> 2 -> 4 -> 5 -> 6 
    """
    adj_matrix = [[0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0]]
    res = topological_sort_khan(adj_matrix)
    assert res == [3, 0, 1, 2, 4, 5, 6]

def test_two_lines():
    """
    3 -> 0 -> 1 -> 2 -> 4   
    5 -> 6 
    """
    adj_matrix = [[0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0]]
    res = topological_sort_khan(adj_matrix)
    assert res == [3, 5, 0, 6, 1, 2, 4]

def test_not_connected():
    adj_matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]
    res = topological_sort_khan(adj_matrix)
    assert res == [0, 1, 2, 3, 4, 5, 6]

def test_general():
    """
    0 -> 2
    1 -> 2 -> 6

    3 -> 4 -> 5 -> 6
    
    """

    adj_matrix = [[0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0]]
    res = topological_sort_khan(adj_matrix)
    assert res == [0, 1, 3, 2, 4, 5, 6]