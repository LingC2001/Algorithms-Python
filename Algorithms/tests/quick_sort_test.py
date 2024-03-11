import pytest
import sys
sys.path.append("./")
from quick_sort import quick_sort_naive, quick_sort_hoare, quick_sort_DNF

def test_empty():
    arr = []
    arr_sorted = sorted(arr)
    quick_sort_naive(arr, 0, len(arr))
    assert arr == arr_sorted

def test_already_sorted():
    arr = [1, 2, 5, 6, 9, 11]
    arr_sorted = sorted(arr)
    quick_sort_naive(arr, 0, len(arr))
    assert arr == arr_sorted

def test_reverse_sorted():
    arr = [19, 11, 8, 5, 2, 0]
    arr_sorted = sorted(arr)
    quick_sort_naive(arr, 0, len(arr))
    assert arr == arr_sorted

def test_normal_sort():
    arr = [1, 7, 2, 8, 7, 1, 4, 10, 22]
    arr_sorted = sorted(arr)
    quick_sort_naive(arr, 0, len(arr))
    assert arr == arr_sorted

def test_negative_nums():
    arr = [1, 7, 2, -8, 7, -1, 4, -10, 22]
    arr_sorted = sorted(arr)
    quick_sort_naive(arr, 0, len(arr))
    assert arr == arr_sorted

def test_negative_nums_only():
    arr = [-1, -7, -2, -8, -7, -1, -4, -10, -22]
    arr_sorted = sorted(arr)
    quick_sort_naive(arr, 0, len(arr))
    assert arr == arr_sorted

def test_decimals():
    arr = [1.4, 7, 2.2, -8.1, 7, -1, 4.0, -10.123, 22]
    arr_sorted = sorted(arr)
    quick_sort_naive(arr, 0, len(arr))
    assert arr == arr_sorted

def test_empty_hoare():
    arr = []
    arr_sorted = sorted(arr)
    quick_sort_hoare(arr, 0, len(arr))
    assert arr == arr_sorted

def test_already_sorted_hoare():
    arr = [1, 2, 5, 6, 9, 11]
    arr_sorted = sorted(arr)
    quick_sort_hoare(arr, 0, len(arr))
    assert arr == arr_sorted

def test_reverse_sorted_hoare():
    arr = [19, 11, 8, 5, 2, 0]
    arr_sorted = sorted(arr)
    quick_sort_hoare(arr, 0, len(arr))
    assert arr == arr_sorted

def test_normal_sort_hoare():
    arr = [1, 7, 2, 8, 7, 1, 4, 10, 22]
    arr_sorted = sorted(arr)
    quick_sort_hoare(arr, 0, len(arr))
    assert arr == arr_sorted

def test_negative_nums_hoare():
    arr = [1, 7, 2, -8, 7, -1, 4, -10, 22]
    arr_sorted = sorted(arr)
    quick_sort_hoare(arr, 0, len(arr))
    assert arr == arr_sorted

def test_negative_nums_only_hoare():
    arr = [-1, -7, -2, -8, -7, -1, -4, -10, -22]
    arr_sorted = sorted(arr)
    quick_sort_hoare(arr, 0, len(arr))
    assert arr == arr_sorted

def test_decimals_hoare():
    arr = [1.4, 7, 2.2, -8.1, 7, -1, 4.0, -10.123, 22]
    arr_sorted = sorted(arr)
    quick_sort_hoare(arr, 0, len(arr))
    assert arr == arr_sorted

def test_empty_DNF():
    arr = []
    arr_sorted = sorted(arr)
    quick_sort_DNF(arr, 0, len(arr))
    assert arr == arr_sorted

def test_already_sorted_DNF():
    arr = [1, 2, 5, 6, 9, 11]
    arr_sorted = sorted(arr)
    quick_sort_DNF(arr, 0, len(arr))
    assert arr == arr_sorted

def test_reverse_sorted_DNF():
    arr = [19, 11, 8, 5, 2, 0]
    arr_sorted = sorted(arr)
    quick_sort_DNF(arr, 0, len(arr))
    assert arr == arr_sorted

def test_normal_sort_DNF():
    arr = [1, 7, 2, 8, 7, 1, 4, 10, 22]
    arr_sorted = sorted(arr)
    quick_sort_DNF(arr, 0, len(arr))
    assert arr == arr_sorted

def test_negative_nums_DNF():
    arr = [1, 7, 2, -8, 7, -1, 4, -10, 22]
    arr_sorted = sorted(arr)
    quick_sort_DNF(arr, 0, len(arr))
    assert arr == arr_sorted

def test_negative_nums_only_DNF():
    arr = [-1, -7, -2, -8, -7, -1, -4, -10, -22]
    arr_sorted = sorted(arr)
    quick_sort_DNF(arr, 0, len(arr))
    assert arr == arr_sorted

def test_decimals_DNF():
    arr = [1.4, 7, 2.2, -8.1, 7, -1, 4.0, -10.123, 22]
    arr_sorted = sorted(arr)
    quick_sort_DNF(arr, 0, len(arr))
    assert arr == arr_sorted