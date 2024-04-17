"""
Selection Sort complexity analysis:

Time complexity:
    For every number, it finds the next minimum value.
    Therefore T(n) = n + (n-1) + (n-2) ... = n(n+1)/2 
    Therefore O(n^2)

Space complexity:
    we do not create any new arrays or anything, it is all done in-place
    Therefore O(1)

"""


def selection_sort(nums):

    for i in range(len(nums)): # array is sorted for idx [0 -> i-1]
        min_val = nums[i]
        min_idx = i
        for j in range(i, len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i] # array is sorted for idx i
        # i increments by 
    # sorted in place, therefore returning nothing.
    return None
