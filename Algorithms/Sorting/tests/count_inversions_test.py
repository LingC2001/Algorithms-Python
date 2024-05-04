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

def test_empty_list():
    assert count_inversions([]) == 0

def test_single_element():
    assert count_inversions([1]) == 0

def test_two_elements_sorted():
    assert count_inversions([1, 2]) == 0

def test_two_elements_unsorted():
    assert count_inversions([2, 1]) == 1

def test_three_elements_sorted():
    assert count_inversions([1, 2, 3]) == 0

def test_three_elements_unsorted():
    assert count_inversions([3, 2, 1]) == 3

def test_large_sorted_list():
    assert count_inversions(list(range(100))) == 0

def test_large_unsorted_list():
    assert count_inversions(list(range(100, 0, -1))) == 4950

def test_list_with_duplicates():
    assert count_inversions([1, 2, 2, 1]) == 2

def test_list_with_negative_numbers():
    assert count_inversions([-1, -2, 0, 1, 2]) == 1

def test_list_with_zero():
    assert count_inversions([0, 0, 0, 0, 0]) == 0