import pytest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from radix_sort import radix_sort
import time

def test_empty_arr():
    s = time.perf_counter()
    arr = []
    assert radix_sort(arr) == []
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_1_digit():
    s = time.perf_counter()
    arr = [2, 4, 1, 9, 4, 0, 3, 0, 4]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_2_digit_repeat():
    s = time.perf_counter()
    arr = [22, 44, 11, 99, 44, 10, 33, 10, 44]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_2_digit_random():
    s = time.perf_counter()
    arr = [43, 13, 64, 22, 64, 92, 17, 50, 38]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_different_size():
    s = time.perf_counter()
    arr = [431, 1341, 642, 224, 64, 9222, 174, 50, 38211]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_large_numbers():
    s = time.perf_counter()
    arr = [43112312, 13414123, 6424132, 22412344, 64123422, 922212344, 1741234, 501234, 38211]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_negative_nums():
    s = time.perf_counter()
    arr = [431, -1341, 642, 224, 64, -9222, 174, -50, 38211]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_negative_nums_only():
    s = time.perf_counter()
    arr = [-431123, -1341, -642, -22422, -6412, -9222, -17433, -50, -38211]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")

def test_sort_large_negative_numbers():
    s = time.perf_counter()
    arr = [-43112312, 13414123, -6424132, 22412344, -64123422, 922212344, -1741234, 501234, -38211]
    assert radix_sort(arr) == sorted(arr)
    print(f"Runtime: {time.perf_counter()-s} s")