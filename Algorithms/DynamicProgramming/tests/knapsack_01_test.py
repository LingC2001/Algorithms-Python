import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from knapsack_01 import knapsack_01
import pytest


def test_no_items():
    weights = []
    values = []
    capacity = 1
    assert knapsack_01(values, weights, capacity) == 0

def test_no_capacity():
    weights = [1]
    values = [100]
    capacity = 0
    assert knapsack_01(values, weights, capacity) == 0

def test_negative_capcity():
    weights = [1]
    values = [100]
    capacity = -1
    assert knapsack_01(values, weights, capacity) == 0

def test_basic():
    weights = [1]
    values = [100]
    capacity = 5
    assert knapsack_01(values, weights, capacity) == 100

def test_multiple_items_1():
    weights = [1, 2, 3]
    values = [100, 201, 300]
    capacity = 5
    assert knapsack_01(values, weights, capacity) == 501

def test_multiple_items_2():
    weights = [1, 2, 3]
    values = [100, 201, 500]
    capacity = 5
    assert knapsack_01(values, weights, capacity) == 701

def test_multiple_items_3():
    weights = [1, 2, 3]
    values = [101, 201, 500]
    capacity = 10
    assert knapsack_01(values, weights, capacity) == 802

def test_same_weights():
    weights = [1, 1, 1]
    values = [100, 102, 101]
    capacity = 2
    assert knapsack_01(values, weights, capacity) == 203

def test_multiple_items_4():
    weights = [5, 1, 2, 3, 10, 4]
    values = [100, 200, 500, 300, 200, 300]
    capacity = 10
    assert knapsack_01(values, weights, capacity) == 1300

def test_multiple_items_5():
    weights = [5, 1, 2, 3, 6, 4]
    values = [100, 200, 500, 300, 500, 300]
    capacity = 9
    assert knapsack_01(values, weights, capacity) == 1200