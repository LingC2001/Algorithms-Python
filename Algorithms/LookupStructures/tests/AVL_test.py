import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from AVL_tree import AVLTree
import pytest

def test1():
    arr = [5, 2, 7, 4, 9, 10, 6]
    bst = AVLTree(arr)
    assert bst.get_sorted_array() == sorted([5, 2, 7, 4, 9, 10, 6])
    assert bst.search(3) == False
    assert bst.search(2) == True
    bst.insert(3)
    assert bst.check_balance() == True
    assert bst.search(3) == True
    assert bst.get_sorted_array() == sorted([5, 2, 7, 4, 9, 10, 6, 3])
    bst.insert(3)
    assert bst.check_balance() == True
    assert bst.search(3) == True
    assert bst.get_sorted_array() == sorted([5, 2, 7, 4, 9, 10, 6, 3])
    bst.insert(11)
    assert bst.check_balance() == True
    assert bst.search(3) == True
    assert bst.search(11) == True
    assert bst.get_sorted_array() == sorted([5, 2, 7, 4, 9, 10, 6, 3, 11])
    bst.insert(12)
    assert bst.check_balance() == True
    bst.insert(13)
    assert bst.check_balance() == True
    bst.insert(14)
    assert bst.check_balance() == True
    bst.insert(15)
    assert bst.check_balance() == True
    bst.insert(16)
    assert bst.check_balance() == True
    bst.insert(17)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 2, 7, 4, 9, 10, 6, 3, 11, 12, 13, 14, 15, 16, 17])
    bst.delete(17)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 2, 7, 4, 9, 10, 6, 3, 11, 12, 13, 14, 15, 16])
    bst.delete(2)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 7, 4, 9, 10, 6, 3, 11, 12, 13, 14, 15, 16])
    bst.delete(11)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 7, 4, 9, 10, 6, 3, 12, 13, 14, 15, 16])
    bst.delete(7)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 4, 9, 10, 6, 3, 12, 13, 14, 15, 16])
    bst.delete(10)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 4, 9, 6, 3, 12, 13, 14, 15, 16])
    bst.delete(13)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 4, 9, 6, 3, 12, 14, 15, 16])
    bst.delete(12)
    bst.delete(14)
    bst.delete(3)
    bst.delete(16)
    bst.delete(15)
    assert bst.check_balance() == True
    assert bst.get_sorted_array() == sorted([5, 4, 9, 6])