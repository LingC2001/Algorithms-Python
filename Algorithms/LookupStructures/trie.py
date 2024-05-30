"""
Trie (Retrieval Tree/ Prefix Tree)

Tries are often implemented in 2 ways, using Arrays and using Hashtables

HashTable vs BST vs Array 

- Traditionally Tries are implemented as Arrays. This is because this method is both fast and memory efficient for:
    - shorter strings
    - evenly distributed strings
    - O(26^N) where N is string size
    - faster access

- Binary search Trees can be used at every node instead
    - if words are sparse, then it saves space since only letters that are being used uses memory
    - However traversal to next node becomes O(log(alphabet))

- Hashtables are the best of both worlds, they have a large overhead, however they are good when:
    - long strings
    - some letters are rarely used and don't need to reserve space for it at every node
    - still O(1) access but need to continually perform hash function.
        - which is basically using an array under it anyway

"""

class Trie(object):
    """
    Array Implementation of a Trie for all lowercase English letters
    """

    def __init__(self):
        self.trie = [False] * 27 # letter is in trie if at the index it is not false
        # word exists in trie depending on value stored in element 27 (last index)
        # ascii a = 97,  z = 122

    def idx(self, c):
        return ord(c)-97

    def insert(self, word):
        """
        Inserts a word into the Trie
        Time Complexity: O(m), where m is the size of word
        Space ComplexityL O(m * TrieNode)
        """
        trie = self.trie
        for i in range(len(word)):
            if trie[self.idx(word[i])] is False:
                trie[self.idx(word[i])] = [False] * 27
            trie = trie[self.idx(word[i])]
        trie[-1] = True

    def delete(self, word):
        """
        Deletes a word into the Trie
        Just turns the indicator to False. This implementation does not
        actually remove the unused nodes. 
        Can be improved by recursively deleting any chains that no longer contain
        a word

        Time Complexity: O(m), where m is the size of word
        Space ComplexityL O(1)
        """
        trie = self.trie
        for i in range(len(word)):
            if trie[self.idx(word[i])] is False:
                return
            else:
                trie = trie[self.idx(word[i])]
        trie[-1] = False

    def search(self, word):
        """
        Checks if a word is in the Trie
        Time Complexity: O(m)
        Space Complexity: O(1)
        """
        trie = self.trie
        for i in range(len(word)):
            if trie[self.idx(word[i])] is False:
                return False
            else:
                trie = trie[self.idx(word[i])]
        return trie[-1]

    def starts_with(self, prefix):
        """
        Checks if any words start with {prefix}
        Time complexity: O(m)
        Space complexity: O(1)
        """
        trie = self.trie
        for i in range(len(prefix)):
            if trie[self.idx(prefix[i])] is False:
                return False
            else:
                trie = trie[self.idx(prefix[i])]
        return True
    
    def get_starts_with(self, prefix):
        """
        Returns all words in the Trie that starts with {prefix}
        
        """
        output = []
        path = []
        trie = self.trie
        for i in range(len(prefix)):
            if trie[self.idx(prefix[i])] is False:
                return []
            else:
                path.append(prefix[i])
                trie = trie[self.idx(prefix[i])]
        
        self.dfs(trie, path, output)
        return output
    
    def get_sorted(self):
        """
        Returns all the words in sorted order.

        Time complexity: O(26 * N), where N is the number of nodes and 26 is the alphabet size
        Space complexity: O(N^2),
            maximum number of words possible is O(N), each word could be up to O(N) in length
        """
        output = []
        self.dfs(self.trie, [], output)
        return output

    def dfs(self, trie, path, output):
        """
        Traverses the trie starting from given node and appends
        all words into output array.
        """
        if trie[-1] is True:
            output.append("".join(path))
        
        for i in range(26):
            if trie[i] is not False:
                path.append(chr(i+97))
                self.dfs(trie[i], path, output)
                path.pop()