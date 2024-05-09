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

def test_empty_graph():
    adj_list = []
    assert topological_sort_dfs(adj_list) == []

def test_single_node():
    adj_list = [[]]
    assert topological_sort_dfs(adj_list) == [0]

def test_two_nodes():
    adj_list = [[1], []]
    assert topological_sort_dfs(adj_list) == [0, 1]

def test_three_nodes():
    adj_list = [[1, 2], [], []]
    assert topological_sort_dfs(adj_list) == [0, 1, 2]

def test_cyclic_graph():
    adj_list = [[1], [2], [0]]
    try:
        topological_sort_dfs(adj_list)
        assert False
    except RecursionError:
        assert True

def test_general_graph():
    adj_list = [[2, 3], [2, 4], [], [4], []]
    res = topological_sort_dfs(adj_list)
    idx = [-1]*len(adj_list)
    for i in range(len(res)):
        idx[res[i]] = i
    
    # check every edge is satisfied
    for u in range(len(adj_list)):
        for v in adj_list[u]:
            assert idx[u] < idx[v]

def test_disconnected_graph():
    adj_list = [[1], [], [3], []]
    res = topological_sort_dfs(adj_list)
    idx = [-1]*len(adj_list)
    for i in range(len(res)):
        idx[res[i]] = i
    
    # check every edge is satisfied
    for u in range(len(adj_list)):
        for v in adj_list[u]:
            assert idx[u] < idx[v]