import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from suffix_trie import SuffixTrie

def test_1():
    st = SuffixTrie("banana")
    assert sorted(st.find("a", "n")) == sorted(["an", "anan", "an"])
    assert st.check_pattern("ana") == True
    assert st.check_pattern("an") == True
    assert st.check_pattern("na") == True
    assert st.check_pattern("ba") == True
    assert st.check_pattern("anana") == True
    assert st.check_pattern("banana") == True
    assert st.check_pattern("b") == True
    assert st.check_pattern("nn") == False
    assert st.check_pattern("c") == False
    assert sorted(st.find("b", "c")) == sorted([])
    assert sorted(st.find("a", "a")) == sorted(["ana", "anana", "ana"])