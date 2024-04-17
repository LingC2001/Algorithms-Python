"""
Insertion Sort complexity analysis:

Time complexity:
    For each element it shuffles it to the correct position. 
    Worst case: O(n^2)
    Best case: O(n), when array is already sorted, the second shuffle loop doesn't occur

Space complexity:
    It is done in-place
    Therefore O(1)

"""

def insertion_sort(nums):
    # idea: shuffle(insert) the current element to the correct position at each iteration
    # Each iteration sorts 1 element 

    for i in range(1, len(nums)):
        # arr is sorted for idx 0 -> i-1
        key = nums[i]
        j = i - 1
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j] 
            j -= 1
        nums[j+1] = key
        # arr is sorted for idx 0 -> i
        # i = i + 1
    return None # sorted in-place
