"""
A Suffix Tree is a compact Suffix Trie, where long sequences of non-branching edges
are compressed into a single edge, represented by start and end indices.

A Suffix Trie is a trie that contains all suffixes of a particular string.
It is useful for pattern matching applications.
This is because any substring of a string is simply a prefix of a suffix.
Therefore creating a Trie (Prefix Trie) containing all suffixes allow us to search for
any substrings in O(m) operations, where m = len(search_pattern)

"""

class suffix_tree:
    pass