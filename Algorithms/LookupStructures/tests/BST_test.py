import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from BST import BST
import pytest

def test1():
    arr = [2, 5, 2, 5, 2, 7, 4, 9, 10, 2, 6]
    bst = BST(arr)

    bst.insert(2)
    assert bst.get_sorted_array() == sorted([2, 2, 5, 2, 5, 2, 7, 4, 9, 10, 2, 6])
    bst.insert(3)
    assert bst.get_sorted_array() == sorted([2, 2, 5, 2, 5, 2, 7, 4, 9, 10, 2, 6, 3])
    bst.delete(11)
    assert bst.get_sorted_array() == sorted([2, 2, 5, 2, 5, 2, 7, 4, 9, 10, 2, 6, 3])
    bst.delete(2)
    assert bst.get_sorted_array() == sorted([5, 5, 7, 4, 9, 10, 6, 3])
    bst.delete(6)
    assert bst.get_sorted_array() == sorted([5, 5, 7, 4, 9, 10, 3])
    bst.insert(6)
    assert bst.get_sorted_array() == sorted([5, 5, 7, 4, 9, 10, 3, 6])
    bst.insert(10)
    assert bst.get_sorted_array() == sorted([5, 5, 7, 4, 9, 10, 3, 6, 10])
    bst.delete(10)
    assert bst.get_sorted_array() == sorted([5, 5, 7, 4, 9, 3, 6])
    bst.delete(5)
    assert bst.get_sorted_array() == sorted([7, 4, 9, 3, 6])
    bst.delete(7)
    assert bst.get_sorted_array() == sorted([4, 9, 3, 6])
    bst.delete(4)
    assert bst.get_sorted_array() == sorted([9, 3, 6])
    bst.delete(6)
    assert bst.get_sorted_array() == sorted([9, 3])
    bst.delete(9)
    assert bst.get_sorted_array() == sorted([3])
    bst.delete(3)
    assert bst.get_sorted_array() == sorted([])
    bst.delete(3)
    assert bst.get_sorted_array() == sorted([])
    bst.insert(3)
    assert bst.get_sorted_array() == sorted([3])
    bst.insert(3)
    assert bst.get_sorted_array() == sorted([3, 3])
    bst.insert(1)
    assert bst.get_sorted_array() == sorted([3, 3, 1])
    
