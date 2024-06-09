
class MinHeap:
    def __init__(self, array):
        # turns the array into a heap in-place
        self.heap = array
        self.size = len(array)
        self.heapify()
        

    def heapify(self):
        """
        Turn the array into a heap.
        Time: O(N)
            - Since down sifting each parent takes O(log(n)) comparisons at most, we can work out
            that the total time complexity of O(N)

        Space: O(1)
        Note that no recursion is used hence no space on the stack is used either, giving us
        auxiliary space complexity of O(1)

        """
        # we perform sift down starting at every parent node going from leaf to the root.
        parent = ((self.size-1)-1)//2 # the last parent is the parent of last leaf
        if parent >= 0:
            for i in range(parent, -1, -1): # for all parents starting from the last parent until 0
                self.sift_down(i)
            

    def pop(self):
        """
        Pop the minimum key from the heap
        Time: O(log(N))
        Space: O(1)
        """
        
        min_pop = None
        if self.size > 0:
            # swap root node with last node of the heap.
            self.swap(0, self.size-1)
            min_pop = self.heap.pop()
            self.size -= 1

            # now sift down the element that got swapped to the root
            self.sift_down(0)
        return min_pop

    def sift_down(self, parent):
        l = 2*parent + 1
        r = 2*parent + 2

        while l < self.size:
            smaller_child = l
            if r < self.size and self.heap[r] < self.heap[l]:
                smaller_child = r
            if self.heap[parent] > self.heap[smaller_child]:
                self.swap(parent, smaller_child)
                parent = smaller_child
                l = 2*parent + 1
                r = 2*parent + 2
            else:
                break


    def insert(self, key):
        """
        Insert a key into the heap
        Time: O(log(N))
        Space: O(1)
        """
        # insert heap at next leaf node
        self.heap.append(key)
        self.size += 1
        self.sift_up(self.size-1)

    def sift_up(self, child_idx):
        # sift up
        i = self.size-1
        parent = (i-1)//2

        while parent>=0 and self.heap[i] < self.heap[parent]:
            # swap parent and child, if child is smaller
            self.swap(i, parent)
            i = parent
            parent = (i-1)//2

    def peek(self):
        if self.size > 0:
            return self.heap[0]
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sort_pop(self):
        """
        "Pop" the minimum key from the heap and place it at the end
        Time: O(log(N))
        Space: O(1)
        """
        
        min_pop = None
        if self.size > 0:
            # swap root node with last node of the heap.
            self.swap(0, self.size-1)
            min_pop = self.heap[self.size-1]
            self.size -= 1

            # now sift down the element that got swapped to the root
            self.sift_down(0)
        return min_pop

    def heap_sort(self):
        """
        Time: O(NLog(N))
        Space: O(1)
            Usually we would need to create output array, which would take auxiliary space,
            but as we pop the elements, we can place it at the back to the original array.
            And then we could reverse it in the end.
                - or if we didn't want to reverse, just use a max heap instead to sort in increasing order
        """
        while self.size > 1:
            self.sort_pop()
        self.heap.reverse()
        return self.heap
        

    