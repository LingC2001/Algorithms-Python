import pytest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from counting_sort import counting_sort
import time

def test_empty_arr():
    s = time.perf_counter()
    arr = []
    assert counting_sort(arr) == []
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort():
    s = time.perf_counter()
    arr = [1, 3, 2, 6, 7, 4]
    assert counting_sort(arr) == [1, 2, 3, 4, 6, 7]
    print(f"Runtime: {time.perf_counter()-s} s")

def test_negative_nums():
    s = time.perf_counter()
    arr = [1, 3, 2, 6, -1, 7, 4, -6]
    assert counting_sort(arr) == [-6, -1, 1, 2, 3, 4, 6, 7]
    print(f"Runtime: {time.perf_counter()-s} s")

def test_already_sorted():
    s = time.perf_counter()
    arr = [1, 2, 3, 5, 8]
    assert counting_sort(arr) == [1, 2, 3, 5, 8]
    print(f"Runtime: {time.perf_counter()-s}")

def test_decreasing():
    s = time.perf_counter()
    arr = [6, 4, 2, 1, -3]
    assert counting_sort(arr) == [-3, 1, 2, 4, 6]
    print(f"Runtime: {time.perf_counter()-s} s")

def test_large_inputs():
    s = time.perf_counter()
    arr = [3,-9223372, 2, -1, 9223368]
    assert counting_sort(arr) == [-9223372, -1, 2, 3, 9223368]
    print(f"Runtime: {time.perf_counter()-s} s")

def test_larger_inputs():
    s = time.perf_counter()
    with pytest.raises(OverflowError):
        arr = [3,-92233720368547758077454574, 2, -1, 9223372036854775804574574577]
        assert counting_sort(arr) == [-92233720368547758077454574, -1, 2, 3, 9223372036854775804574574577]
    print(f"Runtime: {time.perf_counter()-s} s")

def test_decimals():
    s = time.perf_counter()
    with pytest.raises(TypeError):
        arr = [1, 3, 2, 6, 7, 4, 0.1, -9.9, -9.8, -9.3, 1.0, 4.2, 9.3]
        assert counting_sort(arr) == [-9.9, 0.1, 1, 2, 3, 4, 6, 7]
    print(f"Runtime: {time.perf_counter()-s} s")