import pytest
import sys
sys.path.append("./")
from select_min_max import select_min_max

def test_empty():
    arr = []
    with pytest.raises(ValueError):
        arr_min, arr_max = select_min_max(arr)

def test_normal():
    arr = [2, 5, 7, 9, 3, 2, 1, 7]
    arr_min, arr_max = select_min_max(arr)
    assert arr_min == min(arr) and arr_max == max(arr)

def test_negative():
    arr = [-2, 5, 7, 9, -3, 2, 1, -7]
    arr_min, arr_max = select_min_max(arr)
    assert arr_min == min(arr) and arr_max == max(arr)

def test_negative_only():
    arr = [-2, -5, -7, -9, -3, -2, -1, -7]
    arr_min, arr_max = select_min_max(arr)
    assert arr_min == min(arr) and arr_max == max(arr)

def test_one_element():
    arr = [1]
    arr_min, arr_max = select_min_max(arr)
    assert arr_min == min(arr) and arr_max == max(arr)

def test_3_elements():
    arr = [2, -5, 7]
    arr_min, arr_max = select_min_max(arr)
    assert arr_min == min(arr) and arr_max == max(arr)