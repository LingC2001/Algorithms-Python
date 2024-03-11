import sys
sys.path.append("./")
from merge_sort import merge_sort
import pytest

def test_empty_arr():
    arr = []
    assert merge_sort(arr) == []

def test_sort():
    arr = [1, 3, 2, 6, 7, 4]
    assert merge_sort(arr) == [1, 2, 3, 4, 6, 7]

def test_sort_with_negative_nums():
    arr = [1, 3, 2, 6, -1, 7, 4, -6]
    assert merge_sort(arr) == [-6, -1, 1, 2, 3, 4, 6, 7]

def test_already_sorted():
    arr = [1, 2, 3, 5, 8]
    assert merge_sort(arr) == arr

def test_decreasing():
    arr = [6, 4, 2, 1, -3]
    assert merge_sort(arr) == arr[::-1]

def test_large_inputs():
    arr = [3,-9223372036854775807, 2, -1, 9223372036854775807]
    assert merge_sort(arr) == [-9223372036854775807, -1, 2, 3, 9223372036854775807]

def test_larger_inputs():
    arr = [3,-92233720368547758077454574, 2, -1, 9223372036854775804574574577]
    assert merge_sort(arr) == [-92233720368547758077454574, -1, 2, 3, 9223372036854775804574574577]

def test_decimals():
    arr = [1, 3, 2, 6, 7, 4, 0.1, -9.9]
    assert merge_sort(arr) == [-9.9, 0.1, 1, 2, 3, 4, 6, 7]