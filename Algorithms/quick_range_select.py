
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

def quick_range_select(arr, search_range):

    if len(arr) == 0:
        raise IndexError
    if search_range[0] < 0 or search_range[1] > len(arr):
        raise IndexError
    if search_range[1] - search_range[0] <=0:
        return []
    
    _quick_select(arr, 0, len(arr), search_range)
    return arr[search_range[0]:search_range[1]]
    
def _quick_select(arr, lo, hi, search_range):
    """
    selects a range of elements using one call of quick-select
    Logic:
    case 1: drop left side of range[0]
                        piv_left            piv_right
                           |                   |
            [1, 4, 6, 1, 3, 6, 2, 9, 3, 4, 1, 3, 6, 2, 1, 2, 2, 4]
                    |                |
                range[0]           range[1]
    
    case 2: drop right side of range[1]
                        piv_left            piv_right
                           |                   |
            [1, 4, 6, 1, 3, 6, 2, 9, 3, 4, 1, 3, 6, 2, 1, 2, 2, 4]
                                    |                |
                                range[0]           range[1]
    
    case 3: resurse both sides of midleft and midright
                        piv_left            piv_right
                           |                   |
            [1, 4, 6, 1, 3, 6, 2, 9, 3, 4, 1, 3, 6, 2, 1, 2, 2, 4]
                    |                                   |
                range[0]                             range[1]

    case 4: range already found, stop algorithm, return results
                        piv_left            piv_right
                           |                   |
            [1, 4, 6, 1, 3, 6, 2, 9, 3, 4, 1, 3, 6, 2, 1, 2, 2, 4]
                                |           |
                            range[0]      range[1]      
    """

    if hi > lo:
        pivot = arr[random.randint(lo, hi-1)]
        piv_left, piv_right = DNF_partition(arr, lo, hi, pivot)

        if piv_left <= search_range[0] and piv_right < search_range[1]: # pivot is <= lower range, and whole range not found
            # just recurse right half
            _quick_select(arr, piv_right, hi, search_range)
        
        elif piv_right >= search_range[1] and piv_left > search_range[0]: # pivot is >= upper range, and whole range not found
            _quick_select(arr, lo, piv_left, search_range)
        
        elif piv_left > search_range[0] and piv_right < search_range[1]: # recurse both sides
            _quick_select(arr, piv_right, hi, search_range)
            _quick_select(arr, lo, piv_left, search_range)
            
        else: # range we want is within pivots
            return 