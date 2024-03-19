import pytest
import sys
sys.path.append("./")
from quick_select_mom import quick_select_mom

def test_empty():
    arr = []
    k = 1
    with pytest.raises(ValueError):
        quick_select_mom(arr, 0, len(arr), k)
    
def test_out_of_bounds():
    arr = [-9, 2, -1, 3, 4, 7, -5, 6, -8, 0]
    k = 20
    with pytest.raises(IndexError):
        quick_select_mom(arr, 0, len(arr), k)

def test_1():
    arr = [9, 2, 1, 3, 4, 7, 5, 6, 8, 0] # contains nums 0-9
    k = 0
    expected = sorted(arr)[k]
    assert quick_select_mom(arr, 0, len(arr), k) == expected

def test_2():
    arr = [9, 2, 1, 3, 4, 7, 5, 6, 8, 0] # contains nums 0-9
    k = 7
    expected = sorted(arr)[k]
    assert quick_select_mom(arr, 0, len(arr), k) == expected

def test_3():
    arr = [9, 2, 1, 3, 4, 7, 5, 6, 8, 0] # contains nums 0-9
    k = 5
    expected = sorted(arr)[k]
    assert quick_select_mom(arr, 0, len(arr), k) == expected

def test_negatives():
    arr = [-9, 2, -1, 3, 4, 7, -5, 6, -8, 0]
    k = 5
    expected = sorted(arr)[k]
    assert quick_select_mom(arr, 0, len(arr), k) == expected

def test_decimals():
    arr = [-9, 2.1, -1, 3, 4, 7.123, -5.333, 6, -8, 0.0]
    k = 3
    expected = sorted(arr)[k]
    assert quick_select_mom(arr, 0, len(arr), k) == expected

def test_long_arr():
    arr = [9, 2, 1, 3, 4, 7, 5, 6, 8, 0, 2, 4, 12, 41, 2, 123, 1, 2, 2134, 12, 12, 12, 12, 2123, 532, 65, 765, 88, 66, 54, 98, 6, 3, 66, 73, 895, 53, 653]
    k = 15
    expected = sorted(arr)[k]
    assert quick_select_mom(arr, 0, len(arr), k) == expected