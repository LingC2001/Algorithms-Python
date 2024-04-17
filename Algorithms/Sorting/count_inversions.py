"""
Count inversion complexity analysis:

Time complexity:
    Count inversion uses mergesort, only adding a constant time operation of
    count while merging.
    Therefore O(nlog(n))

Space complexityL:
    Same as merge sort
    O(n)

"""


def count_inversions(nums):
    if len(nums) <= 1:
        return 0
    return merge_sort(nums)[1]

def merge_sort(nums):
    if len(nums) <= 1: # base case only 1 element left
        return nums, 0 # already sorted
    else: # more than 1 element left in sub-array, keep splitting
        mid = len(nums)//2
        left, l_count = merge_sort(nums[:mid]) # returns left half sorted
        right, r_count = merge_sort(nums[mid:]) # returns right half sorted
        sorted_arr, count = merge(left, right)
        return sorted_arr, count + l_count + r_count # merge 2 halves
    
def merge(left, right):
    l = 0
    r = 0
    count = 0
    merged = []
    while l <= len(left)-1 or r <= len(right)-1:
        if l >= len(left): # left arr empty
            merged.append(right[r])
            r += 1
        elif r >= len(right): # right arr empty
            merged.append(left[l])
            l += 1
        else:
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
                count += len(left)-l
    return merged, count