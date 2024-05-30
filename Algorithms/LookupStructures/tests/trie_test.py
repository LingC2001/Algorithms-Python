import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from trie import Trie

def test_1():
    trie = Trie()
    trie.insert("hello")
    assert trie.search("hello") == True
    assert trie.search("hell") == False
    assert trie.search("ello") == False
    trie.insert("hell")
    assert trie.search("hello") == True
    assert trie.search("hell") == True
    assert trie.search("ello") == False
    trie.insert("banana")
    assert trie.search("hello") == True
    assert trie.search("hell") == True
    assert trie.search("ello") == False
    assert trie.search("banana") == True
    trie.insert("dream")
    trie.insert("peace")
    trie.insert("triangle")
    trie.insert("drum")
    trie.insert("oath")
    trie.insert("trie")
    trie.insert("drift")
    trie.insert("triangulate")
    # print(trie.get_sorted())
    assert trie.get_sorted() == sorted(["hello", "hell", "banana", "dream", "peace", "triangle", "triangulate", "drum", "oath", "trie", "drift"])
    # print(trie.get_starts_with("tri"))
    assert trie.get_starts_with("tri") == sorted(["trie", "triangle", "triangulate"])
    # print(trie.get_starts_with("tria"))
    assert trie.get_starts_with("tria") == sorted(["triangle", "triangulate"])
    # print(trie.get_starts_with("h"))
    assert trie.get_starts_with("h") == sorted(["hello", "hell"])
    # print(trie.get_starts_with(""))
    assert trie.get_starts_with("") == sorted(["hello", "hell", "banana", "dream", "peace", "triangle", "triangulate", "drum", "oath", "trie", "drift"])
    trie.delete("oaths")
    trie.delete("oath")
    assert trie.get_sorted() == sorted(["hello", "hell", "banana", "dream", "peace", "triangle", "triangulate", "drum", "trie", "drift"])
