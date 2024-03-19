import sys
sys.path.append("./")
from merge_k_sorted import merge_k_sorted
import pytest

def test_normal():
    arrs=[[1,3,5], [1,6,9], [4,7,9,11], [1,1,1,5,6],[2,5,5,5]]
    merged = []
    for arr in arrs:
        merged += arr
    merged.sort()

    assert merge_k_sorted(arrs) == merged

def test_empty():
    arrs=[]
    merged = []
    for arr in arrs:
        merged += arr
    merged.sort()

    assert merge_k_sorted(arrs) == merged

def test_one_arr():
    arrs=[[1,2,6,8,9,12,14,16]]
    merged = []
    for arr in arrs:
        merged += arr
    merged.sort()

    assert merge_k_sorted(arrs) == merged

def test_negative_nums():
    arrs=[[-1,3,5], [-6,-1,9], [-4,7,9,11], [-1,-1,1,5,6],[-2,5,5,5]]
    merged = []
    for arr in arrs:
        merged += arr
    merged.sort()

    assert merge_k_sorted(arrs) == merged