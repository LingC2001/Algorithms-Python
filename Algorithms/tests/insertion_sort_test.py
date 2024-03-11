import pytest
import sys
sys.path.append("./")
from insertion_sort import insertion_sort

def test_empty():
    arr = []
    arr_sorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arr_sorted

def test_already_sorted():
    arr = [1, 2, 5, 6, 9, 11]
    arr_sorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arr_sorted

def test_reverse_sorted():
    arr = [19, 11, 8, 5, 2, 0]
    arr_sorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arr_sorted

def test_normal_sort():
    arr = [1, 7, 2, 8, 7, 1, 4, 10, 22]
    arr_sorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arr_sorted

def test_negative_nums():
    arr = [1, 7, 2, -8, 7, -1, 4, -10, 22]
    arr_sorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arr_sorted

def test_negative_nums_only():
    arr = [-1, -7, -2, -8, -7, -1, -4, -10, -22]
    arr_sorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arr_sorted

def test_decimals():
    arr = [1.4, 7, 2.2, -8.1, 7, -1, 4.0, -10.123, 22]
    arr_sorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arr_sorted