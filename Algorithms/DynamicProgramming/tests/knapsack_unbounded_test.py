import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from knapsack_unbounded import knapsack_unbounded_TD, knapsack_unbounded_BU
import pytest
import math

def test_no_items():
    weights = []
    values = []
    capacity = 1
    assert knapsack_unbounded_TD(values, weights, capacity) == (0, [])
    assert knapsack_unbounded_BU(values, weights, capacity) == (0, [])

def test_no_capacity():
    weights = [1]
    values = [100]
    capacity = 0
    assert knapsack_unbounded_TD(values, weights, capacity) == (0, [])
    assert knapsack_unbounded_BU(values, weights, capacity) == (0, [])

def test_negative_capcity():
    weights = [1]
    values = [100]
    capacity = -1
    assert knapsack_unbounded_TD(values, weights, capacity) == (0, [])
    assert knapsack_unbounded_BU(values, weights, capacity) == (0, [])

def test_basic():
    weights = [1]
    values = [100]
    capacity = 5
    assert knapsack_unbounded_TD(values, weights, capacity) == (500, [0, 0, 0, 0, 0])
    assert knapsack_unbounded_BU(values, weights, capacity) == (500, [0, 0, 0, 0, 0])

def test_multiple_items_1():
    weights = [1, 2, 3]
    values = [100, 201, 300]
    capacity = 5
    assert knapsack_unbounded_TD(values, weights, capacity) == (502, [0, 1, 1])
    assert knapsack_unbounded_BU(values, weights, capacity) == (502, [0, 1, 1])

def test_multiple_items_2():
    weights = [1, 2, 3]
    values = [100, 201, 500]
    capacity = 5
    assert knapsack_unbounded_TD(values, weights, capacity) == (701, [1, 2])
    assert knapsack_unbounded_BU(values, weights, capacity) == (701, [1, 2])

def test_multiple_items_3():
    weights = [1, 2, 3]
    values = [101, 201, 500]
    capacity = 10
    assert knapsack_unbounded_TD(values, weights, capacity) == (1601, [0, 2, 2, 2])
    assert knapsack_unbounded_BU(values, weights, capacity) == (1601, [0, 2, 2, 2])