"""
Quick select (random pivot) complexity analysis

Quick select is very similar to quicksort, however after each partition, 
it drops roughly half of the elements, similar to binary search. E.g.
If we want k = 7th element, and we got our pivot index = 6, then all the elements
to the left of the pivot must not contain the 7th element, therefore can be dropped.

Time complexity:
    Best: O(n), when the first pivot selected is the kth element, then only 1 partitioning is done O(n)
    Average: O(n)
    Worst case: O(n^2), If only one element is dropped per partition

Space complexity:
    If in-place partitioning is used, and no tail-call optimization:
    Best: O(1), when the first pivot selected is the kth element, then no recursive stack
    Average: O(log(n)), if elements are halved every time, then log(n) recursion depth
    Worst: O(n)

"""


import random
def DNF_partition(arr, lo, hi, pivot):
    """
    note: 
    [1:lo+1] will contain elements LESS than pivot
    [lo+1:mid] will contain elements SAME as pivot
    [mid:hi+1] will contain elements that are currently UNDETERMINED
    [hi+1:end] will contain elements MORE than pivot
    """
    mid = lo
    hi = hi-1
    while mid <= hi:
        if arr[mid] < pivot: # red case: smaller therefore swap to the front
            arr[mid], arr[lo] = arr[lo], arr[mid]
            lo += 1
            mid += 1
        elif arr[mid] == pivot: # white case: don't swap because already at correct pos
            mid += 1
        else: # blue case: larger therefore swap to the end
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return lo, mid # return the section that is already sorted
    # lo will end up at the first pivot
    # mid will end up 1 index after pivots

def quick_select_random(arr, lo, hi, k):
    """
    selects the k-th smallest element, not-stable 
    (will need naive-partitioning to be stable)
    """
    if len(arr) == 0:
        raise ValueError
    if k >= len(arr):
        raise IndexError

    if hi > lo:
        pivot = arr[random.randint(lo, hi-1)]
        mid_left, mid_right = DNF_partition(arr, lo, hi, pivot)

        if k < mid_left: # idx we want is to the left of pivots
            return quick_select_random(arr, lo, mid_left, k)
        elif k >= mid_right: # idx we want is to the right of the pivots
            return quick_select_random(arr, mid_right, hi, k)
        else: # idx we want is within pivots
            # k is wihin the pivots, and all the pivots are in the correct positions,
            # therefore arr[k] = arr[mid_left] to arr[mid_right-1], can return any of these
            return arr[k] 
    else:
        return arr[k]