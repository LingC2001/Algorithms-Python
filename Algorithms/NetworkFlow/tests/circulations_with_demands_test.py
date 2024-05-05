import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from circulations_with_demands import circulations_with_demands
import pytest

def test_1():
    G = [[None, (1, 3), (1, 3), None],
         [None, None, (1, 2), (1, 3)],
         [None, None, None, (1, 2)],
         [None, None, None, None]]
    demands = [-4, -3, 2, 5]

    circulation = circulations_with_demands(G, demands)

    assert circulation == [[None, (2,3), (2,3), None],
                           [None, None, (2,2), (3,3)],
                           [None, None, None, (2,2)],
                           [None, None, None, None]]


def test_circulations_with_demands_easy_solution():
    graph = [
        [None, (0, 3), None],
        [(0, 3), None, (0, 3)],
        [None, (0, 3), None]]
    demands = [1, 0, -1]
    assert circulations_with_demands(graph, demands) == [
                                                            [None, (0, 3), None],
                                                            [(1, 3), None, (0, 3)],
                                                            [None, (1, 3), None]]

def test_circulations_with_demands_trivial_solution():
    graph = [
        [None, (0, 1)],
        [(0, 1), None]
    ]
    demands = [0, 0]
    solution =[
        [None, (0, 1)],
        [(0, 1), None]
    ]
    assert circulations_with_demands(graph, demands) == solution

def test_circulations_with_demands_trivial_solution2():
    graph = [
        [None, (0, 2), None],
        [(0, 2), None, (0, 2)],
        [None, (0, 2), None]
    ]
    demands = [0, 0, 0]
    solution = [
        [None, (0, 2), None],
        [(0, 2), None, (0, 2)],
        [None, (0, 2), None]
    ]
    assert circulations_with_demands(graph, demands) == solution


def test_circulations_with_demands_demands_not_zero():
    graph = [
        [None, (0, 1)],
        [(0, 1), None]
    ]
    demands = [1, 1]
    assert circulations_with_demands(graph, demands) == False

def test_circulations_with_demands_5x5_solution():
    graph = [
        [None, (0, 2), None, None, None],
        [(0, 2), None, (0, 3), None, None],
        [None, (0, 3), None, (0, 2), None],
        [None, None, (0, 2), None, (0, 2)],
        [None, None, None, (0, 2), None]
    ]
    demands = [1, 0, -1, 0, 0]
    solution = [
        [None, (0, 2), None, None, None],
        [(1, 2), None, (0, 3), None, None],
        [None, (1, 3), None, (0, 2), None],
        [None, None, (0, 2), None, (0, 2)],
        [None, None, None, (0, 2), None]
    ]
    assert circulations_with_demands(graph, demands) == solution
