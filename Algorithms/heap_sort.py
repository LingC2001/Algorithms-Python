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
