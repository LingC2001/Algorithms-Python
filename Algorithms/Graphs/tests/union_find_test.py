import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from union_find import UnionFind
import pytest

def test_init():
    uf = UnionFind(5)
    assert uf.parent == [0, 1, 2, 3, 4]
    assert uf.rank == [0, 0, 0, 0, 0]
    
def test_union_and_find():
    uf = UnionFind(10)
    uf.union(1,2)
    uf.union(3,4)
    uf.union(5,6)
    uf.union(4,6)

    assert uf.find(1) == uf.find(2)
    assert uf.find(3) == uf.find(4)
    assert uf.find(5) == uf.find(6)
    assert uf.find(4) == uf.find(6)
    assert uf.find(4) == uf.find(5)

