import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from matrix_order import matrix_order
import pytest

# matrices sizes are stored in a list in the form of [(row1, col1), (row2, col2)]

def test_empty():
    matrices = []
    assert matrix_order(matrices) == 0

def test_one_matrix():
    matrices = [(3, 3)]
    assert matrix_order(matrices) == 0

def test_two_matrices():
    matrices = [(3, 3), (3, 4)]
    assert matrix_order(matrices) == 3*3*4

def test_1():
    matrices = [(3, 3), (3, 4), (4, 100)]
    # 3*3*4 + 3*4*100 = 1236
    # 3*3*100 + 3*4*100 = 2100 
    # notice if we multiply the last 2 matrices first, we will end up with a (3,100) matrix
    # then we have to multiple this large matrix again

    assert matrix_order(matrices) == 1236

def test_2():
    matrices = [(4, 2), (2, 5), (5, 3)]
    assert matrix_order(matrices) == 54

def test_3():
    matrices = [(1, 10), (10, 100), (100, 1000), (1000, 10000)]
    assert matrix_order(matrices) == 10_101_000