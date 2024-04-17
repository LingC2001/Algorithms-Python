import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from topological_sort_dfs import topological_sort_dfs
import pytest

def test_empty():
    adj_matrix = []
    adj_list = []
    res = topological_sort_dfs(adj_list)
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
    
    res = topological_sort_dfs(adj_list)
    print(res)
    idx = [-1]*len(adj_matrix)
    for i in range(len(res)):
        idx[res[i]] = i
    
    # check every edge is satisfied
    for u in range(len(adj_matrix)):
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1:
                assert idx[u] < idx[v]

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
    
    res = topological_sort_dfs(adj_list)
    print(res)
    idx = [-1]*len(adj_matrix)
    for i in range(len(res)):
        idx[res[i]] = i
    
    # check every edge is satisfied
    for u in range(len(adj_matrix)):
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1:
                assert idx[u] < idx[v]

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
    
    res = topological_sort_dfs(adj_list)
    print(res)
    idx = [-1]*len(adj_matrix)
    for i in range(len(res)):
        idx[res[i]] = i
    
    # check every edge is satisfied
    for u in range(len(adj_matrix)):
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1:
                assert idx[u] < idx[v]

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
    
    res = topological_sort_dfs(adj_list)
    print(res)
    idx = [-1]*len(adj_matrix)
    for i in range(len(res)):
        idx[res[i]] = i
    
    # check every edge is satisfied
    for u in range(len(adj_matrix)):
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] == 1:
                assert idx[u] < idx[v]