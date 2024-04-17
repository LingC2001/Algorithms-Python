"""
Quick sort time complexity:

Time complexity:
    At each level, the partitioning takes O(n) total time.
    Therefore the time complexity depends entirely on the number of levels,
    which depend on the quality of the pivot.
    Best case: O(nlog(n)), when the pivot is always the median, then the input is halved
    at every level, therfore only log2(n) levels.

    Worst case: O(n^2), when the pivot is always the minimum or maximum, then the input
    is reduced by 1 every level, therefore n levels

    Average case: O(nlog(n)), can be proven using coin-flip argument, assuming theres a
    50% change to get a good pivot and 50% change to get a bad one. (the middle 50% of the
    sorted sequence is a good pivot)


Space complexity:
    The space complexity of quicksort depends on the recursion stack as well as the partitioning
    method used.
    If we used naive partitioning, then we can see that auxiliary space is O(n), because of the new
    array created
    Worst/Avg/Best: O(n)

    If we used Hoare or DNF partitioning, which are in-place, then the aux space is the recursion stack
    depth. When pivot is bad, this could lead to O(n) recursion depth, therefore:
    Worst: O(n)
    Avg/best: O(log(n))

    However, if we performed tail recursion optimization, then we can reduce the worst case
    aux space complexity to be:
    Worst: O(log(n))

"""


def naive_partition(arr, lo, hi, pivot):
    """
    just make 3 lists and go through arr[lo:hi] and append to correct list
    """
    left = []
    pivots = []
    right = []
    for i in range(lo, hi):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            pivots.append(arr[i])
        else:
            right.append(arr[i])
    arr[lo:hi] = left+pivots+right
    return lo + len(left) + len(pivots)//2

def hoare_partition(arr, lo, hi, p):
    """
    swaps an element larger than pivot from the left with an element smaller than pivot from the right.
    """
    arr[lo], arr[p] = arr[p], arr[lo]
    i = lo
    j = hi-1
    while i <= j :
        while i <= j and arr[i] <= arr[p]: # increment until arr[i] is larger than pivot
            i += 1
        while i <= j and arr[j] > arr[p]: # increment until arr[j] is smaller or equal to pivot
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # swapping pivot back to the correct spot (in between left and right)
    # arr[i] contains a value larger than pivot, arr[j] contains a value smaller or equal
    # therefore if at the start we swapped pivot to the front, then we need to swap with arr[j]
    # if we swapped pivot to the back, then we need to swap with arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

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

def quick_sort_naive(arr, lo, hi):
    if hi > lo:
        pivot = arr[lo]
        mid = naive_partition(arr, lo, hi, pivot)
        quick_sort_naive(arr, lo, mid)
        quick_sort_naive(arr, mid+1, hi)

def quick_sort_hoare(arr, lo, hi):
    if hi > lo:
        p = lo
        mid = hoare_partition(arr, lo, hi, p)
        quick_sort_hoare(arr, lo, mid)
        quick_sort_hoare(arr, mid+1, hi)

def quick_sort_DNF(arr, lo, hi):
    if hi > lo:
        pivot = arr[lo]
        mid_left, mid_right = DNF_partition(arr, lo, hi, pivot)
        quick_sort_DNF(arr, lo, mid_left)
        quick_sort_DNF(arr, mid_right, hi)