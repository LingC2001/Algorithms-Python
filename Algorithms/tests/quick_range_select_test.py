import pytest
import sys
sys.path.append("./")
from quick_range_select import quick_range_select

def test_empty():
    arr = []
    k = [1, 2]
    with pytest.raises(IndexError):
        quick_range_select(arr, k)
    
def test_out_of_bounds():
    arr = [-9, 2, -1, 3, 4, 7, -5, 6, -8, 0]
    k = [3, 20]
    with pytest.raises(IndexError):
        quick_range_select(arr, k)

def test_negative_range():
    arr = [-9, 2, -1, 3, 4, 7, -5, 6, -8, 0]
    k = [5, 4]
    assert quick_range_select(arr, k) == []

def test_zero_range():
    arr = [-9, 2, -1, 3, 4, 7, -5, 6, -8, 0]
    k = [4, 4]
    assert quick_range_select(arr, k) == []

def test_1():
    arr = [9, 2, 1, 3, 4, 7, 5, 6, 8, 0] # contains nums 0-9
    k = [3, 7]
    expected = sorted(arr)[k[0]:k[1]]
    assert quick_range_select(arr, k) == expected

def test_2():
    arr = [9, 2, 1, 3, 4, 7, 5, 6, 8, 0] # contains nums 0-9
    k = [5, 9]
    expected = sorted(arr)[k[0]:k[1]]
    assert quick_range_select(arr, k) == expected
    

def test_3():
    arr = [9, 2, 1, 3, 4, 7, 5, 6, 8, 0] # contains nums 0-9
    k = [1, 6]
    expected = sorted(arr)[k[0]:k[1]]
    assert quick_range_select(arr, k) == expected

def test_negatives():
    arr = [-9, 2, -1, 3, 4, 7, -5, 6, -8, 0]
    k = [0, 3]
    expected = sorted(arr)[k[0]:k[1]]
    assert quick_range_select(arr, k) == expected

def test_decimals():
    arr = [-9, 2.1, -1, 3, 4, 7.123, -5.333, 6, -8, 0.0]
    k = [6, 7]
    expected = sorted(arr)[k[0]:k[1]]
    assert quick_range_select(arr, k) == expected