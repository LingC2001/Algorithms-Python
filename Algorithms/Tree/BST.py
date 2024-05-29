"""
Binary Search Tree implementation
Complexities are in each funciton documentation

"""

class Node:
    def __init__(self, val, count=1, left=None, right=None):
        self.val = val
        self.count = count
        self.left = left
        self.right = right

class BST:
    def __init__(self, array):
        """
        Converts an array of numbers into a Binary Search Tree.

        This implementation works with duplicates. 
        Duplicates can be considered easily by adding a count variable to each node,
        or adding a list at each node to store any extra info.
        
        2 Methods:
            Naive:
                Just insert the elements one by one into an empty BST. 
                Each inseretion cost O(N), hence it could be O(N^2) construction
            Divide and Conquer:
                Sort the array,
                then group duplicates,
                then repeatedly choose the middle node as the parent.
                This in fact creates a balanced BST in O(Nlog(N)) time.

        """
        if len(array) == 0:
            self.bst = None
        else:
            array.sort()
            counts = []

            # counting duplicates
            prev = array[0]
            count = 0
            for num in array:
                if num == prev:
                    count += 1
                else:
                    counts.append((prev, count))
                    prev = num
                    count = 1
            counts.append((prev, count)) # adding last number

            self.bst = self.convert(counts, 0, len(counts))

    def convert(self, array, start, end):
        """
        Inputs:
            array: array of elements
            start: start index (inclusive)
            end: end index (exclusive)
        """
        if start < end:
            mid = (start+end)//2
            new_node = Node(array[mid][0], array[mid][1])
            new_node.left = self.convert(array, start, mid)
            new_node.right = self.convert(array, mid+1, end)
            return new_node
        else:
            return None

    def insert(self, key):
        """
        Iterative insertion of a node in BST

        Time complexity O(N)
            Due to case of unbalanced BST
        Space complexity O(1)
            Since we are doing it iteratively

        """
        if self.bst is None:
            self.bst = Node(key, 1)
        else:


            curr = self.bst
            # traverse to the correct position
            while curr:
                if key > curr.val:
                    prev = curr
                    direction = 1
                    curr = curr.right
                elif key < curr.val:
                    prev = curr
                    direction = 0
                    curr = curr.left
                else: # already exists in BST
                    curr.count += 1
                    return

            # add node
            if direction == 0:
                prev.left = Node(key, 1)
            else:
                prev.right = Node(key, 1)

    def delete(self, key):
        """
        Recursive deletion of a node. This deletes all occurrences of a key. Can be modified
        so that it deletes one occurrence by decrementing the count

        1. Search for the node
        2. Check the number of children
        3. If leaf node (no children), just remove;
           If one children, just remove and attach parent to children
           If two children, find the successor (next biggest) and move here, then delete successor node
        
        Time complexity: O(N)
        Space complexity: O(N)
        """

        self.bst = self.aux_delete(self.bst, key)

    
    def aux_delete(self, node, key):
        if node is None:
            return node

        if key > node.val:
            node.right = self.aux_delete(node.right, key)
        elif key < node.val:
            node.left = self.aux_delete(node.left, key)
        else:
            # one or no children
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else: # 2 children
                swap_key, swap_count = self.successor(node)
                node.val = swap_key
                node.count = swap_count

                # delete successor
                node.right = self.aux_delete(node.right, swap_key)
        return node

    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        # print(f'successor: {node.val}, count: {node.count}')
        return node.val, node.count

    def search(self, key):
        # recursive
        # return self.aux_search(self.bst, key)

        # iterative
        """
        Iterative search of the BST to see if key exists or not
        Time Complexity: O(N)
        Space Complexity: O(1)
        
        """
        curr = self.bst
        while curr:
            if key > curr.val:
                curr = curr.right
            elif key < curr.val:
                curr = curr.left
            else:
                return curr.count
        return False # if we reach a None

    def aux_search(self, node, key):
        """
        Searches the BST to see if a key exists or not.
        Time Complexity: O(N) 
            When the BST is very unbalanced, basically a linked list
        Space Complexity: O(N) 
            When the BST is very unbalanced, the recursion depth is O(N).
            Can do iterative instead for better space complexity.
        """
        if node is None:
            return False
        elif key > node.val:
            return self.aux_search(node.right, key)
        elif key < node.val:
            return self.aux_search(node.left, key)
        else: # current key == node.val
            return True
    
    def get_sorted_array(self):
        traversal = []
        self.inorder(self.bst, traversal)
        return traversal
    
    def inorder(self, node, arr):
        if node:
            
            self.inorder(node.left, arr)
            
            for _ in range(node.count):
                arr.append(node.val)
            
            self.inorder(node.right, arr)
