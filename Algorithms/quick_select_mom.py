import random

def quick_select_mom(arr, lo, hi, k):
    """
    Instead of using a random pivot, which could rarely produce O(N^2) in worst case, although it is O(N) on average
    We can use median of medians algorithm to find the exact median in O(N) worst case time.
    This makes it so that when we do quicksort we can achieve worst case time-complexity of O(NLog(N)) instead of O(N^2)
        - although in practise, on average, quicksort with random pivot is still better than with MoM pivot
    """
    if len(arr) == 0:
        raise ValueError
    if k >= len(arr):
        raise IndexError

    if hi > lo:
        pivot = median_of_medians(arr, lo, hi) 
        mid_left, mid_right = DNF_partition(arr, lo, hi, pivot)

        if k < mid_left: # idx we want is to the left of pivots
            return quick_select_mom(arr, lo, mid_left, k)
        elif k >= mid_right: # idx we want is to the right of the pivots
            return quick_select_mom(arr, mid_right, hi, k)
        else: # idx we want is within pivots
            # k is wihin the pivots, and all the pivots are in the correct positions,
            # therefore arr[k] = arr[mid_left] to arr[mid_right-1], can return any of these
            return arr[k] 
    else:
        return arr[k]

def median_of_medians(arr, lo, hi):
    if hi-lo < 5:
        return median_of_five(arr, lo, hi)
    else:
        medians = []
        i = lo
        while i < hi:
            j = min(i+5, hi)
            median = median_of_five(arr, i, j)
            medians.append(median)
            i+=5
        n = len(medians)

        return quick_select_mom(medians, 0, n, n//2)

def median_of_five(arr, lo, hi):
    # insertion sort then get middle element   

    for i in range(lo+1, hi):
            key = arr[i]
            j = i - 1
            while j>=lo and arr[j] > key:
                arr[j+1] = arr[j] 
                j -= 1
            arr[j+1] = key
    
    return arr[(lo+hi)//2]


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

    