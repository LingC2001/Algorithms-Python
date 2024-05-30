"""
A Suffix Trie is a trie that contains all suffixes of a particular string.
It is useful for pattern matching applications.
This is because any substring of a string is simply a prefix of a suffix.
Therefore creating a Trie (Prefix Trie) containing all suffixes allow us to search for
any substrings in O(m) operations, where m = len(search_pattern)
"""

class SuffixTrie:
    def __init__(self, string):
        """

        :Input:
            string: a non-empty string consisting of letters [a-z].
        
        :Postcondition: Custom suffix trie with indices lists is created.

        :Time Complexity: O(N^2), (Best and Worst case)
                          where N is the number of characters in genome string
        :Time Complexity Analysis:
            The time complexity is dominated by the naive suffix trie construction. 
            We use 2 nested for loops to iterate over all non-empty suffixes of the genome string.
            This is at most O(N^2) number of characters checked/trie nodes created. 
                Creating a trie node is simply creating a constant size 5 list, which is O(1).
                The index is appended to the end of the indices list, therefore O(1).
            Therefore in total, the BEST and WORST case time complexity is O(N^2)
        
        :Space Complexity: O(N^2), (Best and Worst case)
                           where N is the number of characters in genome string
        :Space Complexity Analysis:
            The input genome string itself uses O(N) space complexity. Assigning a reference
            to this string as an instance variable (self.genome) uses O(1) auxiliary space.

            The memory usage is dominated by the suffix trie, which can be split into 2 parts:
                1. Trie node lists containing references to other lists:
                    In the worst case when every character in the suffixes create a new trie node,
                    O(N^2) trie nodes would be created. Each trie node is a list of 27 references.
                    Hence O(27*N^2) = O(N^2)
                    In the best case, when the string contains only 1 unique character, e.g. "AAAA",
                    only N trie nodes would be created, hence O(27*N) = O(N)

                2. Indices lists within the trie nodes:
                    Exactly 1 index integer is stored for every character in the suffixes. There
                    are a total of O(N^2) characters in all suffixes, therefore this always uses
                    O(N^2) auxiliary space.
            In total BEST and WORST case: O(N^2) space and auxiliary space complexity.

        """
        self.string = string
        self.suffix_trie = [None]*26
        n = len(string)
        for i in range(n):
            trie = self.suffix_trie
            for j in range(i, n):
                idx = self.char2idx(string[j])
                if trie[idx] is None:
                    trie[idx] = [None]*26 + [[]]
                trie = trie[idx]
                trie[-1].append(j)

    def find(self, start, end):
        """
        Function description:
            Returns all substrings within the string that has a prefix of {start} and a suffix of {end}.
            The algorithm finds the indices of all occurrences of the given prefix, as well as all occurrences of the
            given suffix if they exist.
            Then string slicing is performed based on these 2 indices if they do not result in an overlap of
            the prefix and suffix. The sorted property of the indices list is utilised so that unnecessary checks are avoided.       
                
        :Input:
            start: a non-empy string consisting of only characters [A-D] specifying the search prefix.

            end: a non-empy string consisting of only characters [A-D] specifying the search suffix.
        
        :Output:
            sub_strings: a list of ALL substrings of string that has the specified non-overlapping start prefix and end suffix.

        :Time Complexity: O(T + U + V),
                          where T is the number of characters in the start prefix,
                          where U is the number of characters in the end suffix,
                          where V is the number of characters in the output list.
        :Time Complexity Analysis:
            Since the suffix trie is created using array implementation, where the 4 characters are mapped to the index based 
            on their ASCII values, traversing to each node is O(1). 
            Therefore, traversing and finding the start prefix of size T would be O(T),
            and traversing and finding the end suffix of size U would be O(U).

            Leveraging the sorted property of the indices lists, the valid substrings are considered first and whenever the indices
            result in an overlap of the prefix and suffix, we perform early stopping. 
            Therefore the time complexity of getting the output is simply string slicing all the substrings and appending them
            to the output list. String slicing takes O(k) time complexity for a slice of size k, therefore since the output
            list has a total of V characters, then the time complexity needed for string slicing V characters must be O(V).
            
            The time complexity needed to append all the substrings to the output list must also be bounded by O(V). This is because
            since the substrings must be non-empty (at least size 2), then there must be a maximum of V/2 substrings for a total
            of V characters. Thus we at most append to the output list only O(V/2) times. Hence O(V)

            Therefore in total the time complexity is O(T + U + V).

        :Auxililary Space Complexity: O(V),
                                     where V is the number of characters in the output list.
        :Auxiliary Space Complexity Analysis:
            Except for the output list, everything else creates constant extra auxiliary space. Even the prefix and suffix
            indices lists are just refrences to the lists in the suffix trie. 

            The output list contains V characters, therefore O(V) auxiliary space is used to create this output list of
            substrings. 
        
        :Space Complexity with Inputs: O(N^2 + T + U + V) = O(N^2 + V)
            Where N is the length of the string. Since self is passed in, the space complexity of the object instance,
            which is dominated by the suffix trie is included in the total space complexity.
        """
        # Checking if basic string is long enough
        prefix_len, suffix_len = len(start), len(end)
        min_len = prefix_len + suffix_len
        if len(self.string) < min_len:
            return []

        # searching for start string and getting start indices
        trie = self.suffix_trie
        for c in start:
            idx = self.char2idx(c)
            if trie[idx] is None: # start substring doesn't exist
                return [] 
            trie = trie[idx]
        prefix_indices = trie[-1]

        # searching for end string and getting end indices
        trie = self.suffix_trie
        for c in end:
            idx = self.char2idx(c)
            if trie[idx] is None: # end substring doesn't exist
                return [] 
            trie = trie[idx]
        suffix_indices = trie[-1]

        # getting all valid substrings
        sub_strings = []
        i = 0
        while i < len(prefix_indices) and suffix_indices[-1] >= (prefix_indices[i]+suffix_len):
            j = len(suffix_indices)-1
            while j >= 0 and suffix_indices[j] >= (prefix_indices[i]+suffix_len):
                # slicing substring of string if prefix/suffix do not overlap
                sub_strings.append(self.string[prefix_indices[i]-(prefix_len-1): suffix_indices[j]+1]) 
                j -= 1
            i += 1
        return sub_strings

    def check_pattern(self, pattern):
        trie = self.suffix_trie
        for c in pattern:
            idx = self.char2idx(c)
            if trie[idx] is None: # pattern doesn't exist
                return False
            trie = trie[idx]
        return True

    def char2idx(self, char):
        return ord(char)-97