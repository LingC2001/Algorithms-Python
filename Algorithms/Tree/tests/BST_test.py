import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from BST import BST
import pytest

def test1():
    arr = [2, 5, 2, 5, 2, 7, 4, 9, 10, 2, 6]
    bst = BST(arr)
    assert bst.search(2) == arr.count(2)
    assert bst.search(3) == False
    assert bst.search(7) == arr.count(7)
    assert bst.search(4) == arr.count(4)

    bst.insert(2)
    assert bst.search(2) == arr.count(2)+1
    bst.insert(3)
    assert bst.search(3) == 1
    assert bst.search(7) == arr.count(7)
    assert bst.search(4) == arr.count(4)
    assert bst.search(2) == arr.count(2)+1

    bst.delete(3)
    assert bst.search(3) == False
    bst.delete(2)
    assert bst.search(2) == False
    bst.insert(2)
    assert bst.search(2) == 1
