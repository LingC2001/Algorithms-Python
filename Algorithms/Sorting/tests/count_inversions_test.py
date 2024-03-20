import pytest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from count_inversions import count_inversions

def test_empty_arr():
    arr = []
    assert count_inversions(arr) == 0

def test_single_element():
    arr = [1]
    assert count_inversions(arr) == 0

def test_sorted():
    arr = [-5, -2, 0, 4, 9]
    assert count_inversions(arr) == 0

def test_reversed():
    arr = [3, 2, 1]
    assert count_inversions(arr) == 3

def test_normal():
    arr = [1, 4, 7, -2, 10, 3]
    assert count_inversions(arr) == 6

def test_only_negative_numbers():
    arr = [-3, -2, -10, -4, -6]
    assert count_inversions(arr) == 7