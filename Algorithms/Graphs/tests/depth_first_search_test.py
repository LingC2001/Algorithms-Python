import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from depth_first_search import depth_first_search
import pytest

def test_empty():
    adj_matrix = []
    adj_list = []
    res = depth_first_search(adj_list)
    assert res == []

def test_1():
    # vertex 0 is connected to all other vetices
    # adj_matrix = [[0, 1, 1, 1, 1],
    #               [1, 0, 0, 0, 0],
    #               [1, 0, 0, 0, 0],
    #               [1, 0, 0, 0, 0],
    #               [1, 0, 0, 0, 0]]
    adj_list = [[1, 2, 3, 4],
                [0],
                [0],
                [0],
                [0]]
    res = depth_first_search(adj_list)
    assert res == [0, 1, 2, 3, 4]

def test_2():
    # vertex 0 is connected to 1, which is connected to 3, which is connected to 2
    # vertex 4 is not connected to anything but is still traversed since the algorithm
    # is designed to traverse all nodes even if they are not connected
    # adj_matrix = [[0, 1, 1, 0, 0],
    #               [1, 0, 0, 1, 0],
    #               [1, 0, 0, 1, 0],
    #               [0, 1, 1, 0, 0],
    #               [0, 0, 0, 0, 0]]

    adj_list = [[1, 2],
                [0, 3],
                [0, 3],
                [1, 2],
                []]
    res = depth_first_search(adj_list)
    assert res == [0, 1, 3, 2, 4]

def test_3():
    # adj_matrix = [[0, 1, 0, 0, 0],
    #               [1, 0, 0, 1, 0],
    #               [0, 0, 0, 0, 0],
    #               [0, 1, 0, 0, 1],
    #               [0, 0, 0, 1, 0]]

    adj_list = [[1],
                [0, 3],
                [],
                [1, 4],
                [3]]
    
    res = depth_first_search(adj_list)
    assert res == [0, 1, 3, 4, 2]