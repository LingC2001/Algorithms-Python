
"""
AVL Tree implementation
Complexities are in each funciton documentation
Unlike the BST implementation, for simplicity, this one assumes no duplicates

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

class AVLTree:
    def __init__(self, array):
        """
        Converts an array of numbers into an AVL Tree.
        
        Divide and Conquer:
            Sort the array,
            then repeatedly choose the middle node as the parent.
            This in fact creates a balanced BST in O(Nlog(N)) time.
        """

        if len(array) == 0:
            self.bst = None
        else:
            array.sort()
            self.bst = self.convert(array, 0, len(array))

    def convert(self, array, start, end):
        """
        Inputs:
            array: array of elements
            start: start index (inclusive)
            end: end index (exclusive)
        """
        if start < end:
            mid = (start+end)//2
            new_node = Node(array[mid])
            new_node.left = self.convert(array, start, mid)
            new_node.right = self.convert(array, mid+1, end)
            new_node.height = max(self.get_height(new_node.left), self.get_height(new_node.right)) +1
            return new_node
        else:
            return None
        
    def search(self, key):
        # recursive
        # return self.aux_search(self.bst, key)

        # iterative
        """
        Iterative search of the BST to see if key exists or not
        Time Complexity: O(Log(N)) since AVL maintains a balanced BST
        Space Complexity: O(1)
        
        """
        curr = self.bst
        while curr:
            if key > curr.val:
                curr = curr.right
            elif key < curr.val:
                curr = curr.left
            else:
                return True
        return False # if we reach a None

    def aux_search(self, root, key):
        """
        Searches the BST to see if a key exists or not.
        Time Complexity: O(Log(N)) 
        Space Complexity: O(Log(N)) 
            Can do iterative instead for better space complexity.
        """
        if root is None:
            return False
        elif key > root.val:
            return self.aux_search(root.right, key)
        elif key < root.val:
            return self.aux_search(root.left, key)
        else: # current key == root.val
            return True
    
    def get_height(self, root):
        """
        Returns the height of a node. 
        A leaf node has a height of 1
        """
        if root is None:
            return 0
        else:
            return root.height

    def get_balance(self, root):
        """
        Returns the balance factor of a node.
            balance_factor = height(root.left) - height(root.right)
        """
        if root is None:
            return 0
        else:
            return self.get_height(root.left) - self.get_height(root.right)

    def get_sorted_array(self):
        """
        Returns the array of numbers in sorted order
        """
        traversal = []
        self.inorder(self.bst, traversal)
        return traversal
    
    def inorder(self, root, arr):
        """
        Traverses the AVL Tree using inorder traversal
        """
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
    
    def insert(self, key):
        """
        Inserts a key into the AVL Tree
        If the key already exists, then do nothing
        After inserting, recursively rebalance the tree from bottom up

        Time complexity: O(Log(N))
            Finding insertion position: O(Log(N))
            Max number of rebalances: O(Log(N))
            Every rebalance: O(1)
        
        Space complexity: O(Log(N))
            Recursion depth of balanced BST
        """
        self.bst = self.aux_insert(self.bst, key)
        
    def aux_insert(self, root, key):
        """
        Recursive auxiliary function for inserting
        """
        if root is None: # insert here as a leaf root
            return Node(key)
        elif key > root.val:
            root.right = self.aux_insert(root.right, key)
        elif key < root.val:
            root.left = self.aux_insert(root.left, key)
        else: # if already exists, do nothing
            return root
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        return self.rebalance(root)

    def delete(self, key):
        """
        Deletes a key from the AVL Tree
        If the key doesn't exist, then do nothing
        After deleting, recursively rebalance the tree from bottom up

        Time complexity: O(Log(N))
            Delete node: O(Log(N))
            Max number of rebalances: O(Log(N))
            Every rebalance: O(1)
        
        Space complexity: O(Log(N))
            Recursion depth of balanced BST
        """

        self.bst = self.aux_delete(self.bst, key)

    def aux_delete(self, root, key):
        """
        Recursive auxiliary function for deleting a node with a specific key
        """
        if root is None: # if node not found
            return None
        elif key > root.val:
            root.right = self.aux_delete(root.right, key)
        elif key < root.val:
            root.left = self.aux_delete(root.left, key)
        else: # current node == key, delete it 
            # one or no children
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else: # 2 children
                root.val = self.successor(root)
                # delete successor
                root.right = self.aux_delete(root.right, root.val)
                           
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return self.rebalance(root)
    
    def successor(self, node):
        """
        Finds the successor (next biggest number) of root

        Time complexity: O(Log(N))
        Space complexity: O(1)
        """
        node = node.right
        while node.left:
            node = node.left
        return node.val


    def check_balance(self):
        """
        Checks if the tree is balanced by traversing to every node and checking
        the balance factor
        """
        return self.aux_check_balance(self.bst)

    def aux_check_balance(self, root):
        """
        Auxiliary function for checking if the tree is balanced
        """
        if root is None:
            return True
        else:
            balance = self.get_balance(root)
            if balance >= 2 or balance <=-2:
                return False
            return self.aux_check_balance(root.left) and self.aux_check_balance(root.right)

    def rebalance(self, root):
        """
        Function to rebalance at the current node.
        It checks the balance factors or the current node and the children to determine which
        case it is. 
        Then performs the corresponding rotations needed to rebalance the node.
        Returns the new root after rebalancing.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        balance = self.get_balance(root)

        if balance >= 2:
            if self.get_balance(root.left) >= 0: # left-left case
                # do right rotation
                return self.rotate_right(root) # return the new root so the parent can connect to it
            else: # left-right case
                # rotate left for left subtree to convert it into a left-left case
                root.left = self.rotate_left(root.left)
                # now it is a left-left case therefore rotate right
                return self.rotate_right(root)
        elif balance <= -2:
            if self.get_balance(root.right) <= 0: # right-right case
                # do left rotation
                return self.rotate_left(root)
            else: # right-left case
                # rotate right for right subtree to convert into a right-right case
                root.right = self.rotate_right(root.right)
                # now it is a right-right case therefore rotate left
                return self.rotate_left(root)
        else:
            return root
                
    def rotate_right(self, root):
        pivot = root.left
        temp = pivot.right
        pivot.right = root
        root.left = temp

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        pivot.height = max(self.get_height(pivot.left), self.get_height(pivot.right)) + 1
        return pivot
    
    def rotate_left(self, root):
        pivot = root.right
        temp = pivot.left
        pivot.left = root
        root.right = temp

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        pivot.height = max(self.get_height(pivot.left), self.get_height(pivot.right)) + 1
        return pivot
