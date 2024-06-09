import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from min_heap import MinHeap
import pytest

def test_empty():
    arr = []
    min_heap = MinHeap(arr)
    assert min_heap.pop() == None
    assert min_heap.peek() == None
    min_heap.insert(3)
    assert min_heap.pop() == 3
    assert min_heap.pop() == None

def test_1():
    arr = [1, 3, 5, 1, 8, -3, -7, 10, -2, -1, 2, -1, 5, 8, 9, 3, 4, 7]
    min_heap = MinHeap(arr)
    assert min_heap.peek() == -7
    assert min_heap.pop() == -7
    assert min_heap.pop() == -3
    assert min_heap.pop() == -2
    min_heap.insert(-3)
    min_heap.insert(0)
    assert min_heap.pop() == -3
    assert min_heap.pop() == -1
    assert min_heap.pop() == -1
    assert min_heap.pop() == 0
    assert min_heap.pop() == 1
    print(arr)

def test_sort():
    arr = [1, 3, 5, 1, 8, -3, -7, 10, -2, -1, 2, -1, 5, 8, 9, 3, 4, 7]
    sorted_arr = sorted(arr)
    
    min_heap = MinHeap(arr)
    assert min_heap.heap_sort() == sorted_arr