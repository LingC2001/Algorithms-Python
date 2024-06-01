import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from suffix_array import SuffixArray

def check_sorted(sa):
    for i in range(len(sa.suffix_arr)-1):
        if sa.string[sa.suffix_arr[i]:] > sa.string[sa.suffix_arr[i+1]:]:
            return False
    return True

def test_1():
    sa = SuffixArray("MISSISSIPPI")
    sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)
    
    sa = SuffixArray("CAMEL")
    sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)

    sa = SuffixArray("BANANA")
    sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)

    sa = SuffixArray("jkasdhfoiweAJKSHDiawebiweIASDHIWQu")
    sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)