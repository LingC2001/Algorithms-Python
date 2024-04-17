import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from topological_sort_khan import topological_sort_khan
import pytest

def test_empty():
    adj_matrix = []
    adj_list = []
    res = topological_sort_khan(adj_list)
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
    
    adj_list = [[1],
                [2],
                [4],
                [0],
                [5],
                [6],
                []]

    res = topological_sort_khan(adj_list)
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
    adj_list = [[1],
                [2],
                [4],
                [0],
                [],
                [6],
                []]
    
    res = topological_sort_khan(adj_list)
    assert res == [3, 5, 0, 6, 1, 2, 4]

def test_not_connected():
    adj_matrix = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]
    adj_list = [[],
                [],
                [],
                [],
                [],
                [],
                []]
    res = topological_sort_khan(adj_list)
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
    
    adj_list = [[2],
                [2],
                [6],
                [4],
                [5],
                [6],
                []]
    
    res = topological_sort_khan(adj_list)
    assert res == [0, 1, 3, 2, 4, 5, 6]