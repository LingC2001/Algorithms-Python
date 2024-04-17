"""
Heap Sort complexity analysis:

Time complexity:
    Heapsort first heapifies the array, which is O(n)
    Heapsort extracts the minimum element from the heap n-times.
    Which would be worst case: O(n log(n)), since each get_min is O(log(n))
    However best case: O(n), when all elements in heap are identical, then get_min
    would be O(1).
    Worst case: O(nlog(n))
    Best case: O(n)

Space complexity:
    Since heapify is done in-place, heapsort actually has O(1) auxiliary space complexity.
    

"""


import heapq

def heap_sort_py(nums):
    # we use a max heap because we want to start with the maximum number by putting
    # them to the end, that way we can do it in-place
    # However, can't seem to find a way to do that without modifying how heapq works
    # so therefore going to do it with O(N) aux space

    heapq.heapify(nums) # O(N) heapify
    res = []
    for i in range(len(nums)): # N elements
        res.append(heapq.heappop(nums)) # O(Log(N))
    return res

def heap_sort(nums):
    pass
